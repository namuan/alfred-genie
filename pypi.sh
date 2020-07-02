#!/bin/bash
docker build -f ./Dockerfile.buildenv -t namuan/pypi:build .
docker run --rm -it --entrypoint python namuan/pypi:build setup.py publish
