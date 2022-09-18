#!/bin/bash
docker run -it -v $(pwd):/code -p 8000:8000 nsfw_backend3.8:latest
