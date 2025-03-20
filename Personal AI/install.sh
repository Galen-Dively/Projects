#!/bin/bash

docker run -d -p 5555:11434 --name model ollama/ollama:latest
docker exec -it model ollama pull mistral