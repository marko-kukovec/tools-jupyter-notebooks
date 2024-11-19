#!/bin/sh

for file in protos/*.proto; do
    if [ -f "$file" ]; then
        protoc --proto_path=protos --python_out=protos_bin $file
    fi
done