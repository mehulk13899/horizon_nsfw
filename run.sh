#!/bin/bash
docker run -it -v $(pwd):/code -p 9000:9000 nsfw_backend3.8:latest
