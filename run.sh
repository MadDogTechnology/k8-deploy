#!/bin/bash

docker run \
  --name deploy-kubernetes \
  --volume $PWD:/usr/src/app \
  --env-file="./app.env" \
  --rm \
  deploy-kubernetes \
  python3 /usr/src/app/main.py
