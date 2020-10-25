#!/bin/bash

docker run -dit --rm --privileged --security-opt seccomp=unconfined -h {"$USER"} -p 8080:80 -p 2222:22 -e ALLOWED_NETWORKS=0.0.0.0/0 cultholmes/progressive_minds