# DevOps Docker Container Registry

[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-000000.svg)](https://flask.palletsprojects.com/)
[![Docker API](https://img.shields.io/badge/API-Distribution_V2-blue.svg)](https://docs.docker.com/registry/spec/api/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A **production-grade private container registry** implementation. This repository features a lightweight Docker Registry V2 API compliant server built with Flask, capable of handling `docker push` and `docker pull` commands for local storage.

## 🚀 Features

- **Docker V2 API Support**: Implements core endpoints for image distribution.
- **Local File Storage**: Stores image layers and manifests on the local filesystem.
- **Layer Deduplication**: Efficient storage by hashing layers (SHA256).
- **Concurrency**: Parallel layer uploads supported via Flask threading.
- **Authentication**: Basic Auth hook (mock implementation).

## 📁 Project Structure

```
devops-docker-container-registry/
├── src/
│   ├── registry.py    # Flask API Routes
│   ├── storage.py     # Layer Storage Backend
│   └── main.py        # Entrypoint
├── storage/           # Image Data
├── requirements.txt
└── Dockerfile
```

## 🛠️ Quick Start

```bash
# Clone
git clone https://github.com/Shivay00001/devops-docker-container-registry.git

# Install
pip install -r requirements.txt

# Run Registry (Port 5000)
python src/main.py

# Docker Interaction
docker tag alpine:latest localhost:5000/alpine:latest
docker push localhost:5000/alpine:latest
```

## 📄 License

MIT License
