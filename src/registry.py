import os
import uuid
from flask import Flask, request, jsonify, Response
from src.storage import LocalStorage

app = Flask(__name__)
storage = LocalStorage()

@app.route("/v2/", methods=["GET"])
def api_version_check():
    """Docker Client check for V2 API support."""
    return jsonify({}), 200, {"Docker-Distribution-Api-Version": "registry/2.0"}

@app.route("/v2/<name>/manifests/<reference>", methods=["PUT", "GET"])
def schema_manifest(name, reference):
    if request.method == "PUT":
        manifest = request.json
        storage.save_manifest(name, reference, manifest)
        # Calculate digest of manifest for return
        return "", 201, {"Location": f"/v2/{name}/manifests/{reference}", "Docker-Content-Digest": "sha256:mockdigest"}
    
    elif request.method == "GET":
        manifest = storage.get_manifest(name, reference)
        if manifest:
             # Content-Type must be correct for Docker to accept it
            return jsonify(manifest), 200, {"Content-Type": "application/vnd.docker.distribution.manifest.v2+json"}
        return jsonify({"errors": [{"code": "MANIFEST_UNKNOWN"}]}), 404

@app.route("/v2/<name>/blobs/<digest>", methods=["GET", "HEAD"])
def blob_check(name, digest):
    if request.method == "HEAD":
        if storage.layer_exists(digest):
            return "", 200, {"Content-Length": "0"} # Should be actual length
        return "", 404
    
    # GET
    layer = storage.get_layer(digest)
    if layer:
        return layer, 200
    return "", 404

@app.route("/v2/<name>/blobs/uploads/", methods=["POST"])
def initiate_upload(name):
    # Start upload
    uuid_str = str(uuid.uuid4())
    return "", 202, {"Location": f"/v2/{name}/blobs/uploads/{uuid_str}", "Docker-Upload-Uuid": uuid_str}

@app.route("/v2/<name>/blobs/uploads/<uuid_str>", methods=["PUT", "PATCH"])
def upload_blob(name, uuid_str):
    # Simplified: We treat PUT as final upload with digest
    digest = request.args.get("digest")
    if request.method == "PUT" and digest:
        storage.save_layer(digest, request.data)
        return "", 201, {"Location": f"/v2/{name}/blobs/{digest}", "Docker-Content-Digest": digest}
    
    # PATCH is chunked upload - mock generic success
    return "", 202, {"Location": f"/v2/{name}/blobs/uploads/{uuid_str}", "Docker-Upload-Uuid": uuid_str}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
