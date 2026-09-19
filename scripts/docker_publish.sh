#!/bin/bash
# Builds and pushes multi-architecture Docker images (e.g., for Raspberry Pi/Jetson)

set -e

IMAGE_NAME="ghcr.io/yourusername/smoke-detector-x"
TAG=$(git rev-parse --short HEAD)
LATEST_TAG="latest"

echo "Building and pushing Docker image for arm64 and amd64..."

# Ensure buildx is configured
docker buildx create --use || true

docker buildx build \
  --platform linux/arm64,linux/amd64 \
  --tag ${IMAGE_NAME}:${TAG} \
  --tag ${IMAGE_NAME}:${LATEST_TAG} \
  --push \
  .

echo "Successfully published ${IMAGE_NAME}:${TAG} to registry."
