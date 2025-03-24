#!/bin/bash

set -e
export AWS_ACCOUNT=""
export AWS_DEFAULT_REGION="eu-west-2"
export SERVICE_NAME="api2"
export SERVICE_VERSION="${SERVICE_VERSION:-latest}"
export IMAGE_NAME="$AWS_ACCOUNT.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/stockapi:${SERVICE_NAME}_${SERVICE_VERSION}"

aws ecr get-login-password | docker login --username AWS --password-stdin "$AWS_ACCOUNT.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com"
docker build -t $IMAGE_NAME .
docker push $IMAGE_NAME
