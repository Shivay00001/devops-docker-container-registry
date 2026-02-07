import os
import hashlib
import json

class LocalStorage:
    def __init__(self, root_dir="storage"):
        self.root = root_dir
        os.makedirs(os.path.join(self.root, "layers"), exist_ok=True)
        os.makedirs(os.path.join(self.root, "manifests"), exist_ok=True)

    def save_layer(self, digest, data):
        path = os.path.join(self.root, "layers", digest)
        with open(path, "wb") as f:
            f.write(data)
        return path

    def get_layer(self, digest):
        path = os.path.join(self.root, "layers", digest)
        if os.path.exists(path):
            with open(path, "rb") as f:
                return f.read()
        return None

    def save_manifest(self, name, reference, manifest):
        repo_dir = os.path.join(self.root, "manifests", name)
        os.makedirs(repo_dir, exist_ok=True)
        path = os.path.join(repo_dir, reference)
        with open(path, "w") as f:
            json.dump(manifest, f)
        return path

    def get_manifest(self, name, reference):
        path = os.path.join(self.root, "manifests", name, reference)
        if os.path.exists(path):
            with open(path, "r") as f:
                return json.load(f)
        return None
        
    def layer_exists(self, digest):
        return os.path.exists(os.path.join(self.root, "layers", digest))
