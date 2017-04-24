#!/bin/bash

docker run \
  -it \
  --name deploy-kubernetes \
  --volume $PWD:/usr/src/app \
  --env-file="./app.env" \
  --rm \
  deploy-kubernetes \
  python3 -m pdb /usr/src/app/main.py
