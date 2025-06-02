#!/bin/bash
uv pip install \
  --no-installer-metadata \
  --no-compile-bytecode \
  --target packages \
  -r pyproject.toml

cd packages
zip -r ../package.zip .
cd ..

zip -rg package.zip src/

aws s3 cp package.zip s3://abstractabstraction-data

rm -r packages
rm package.zip

# aws lambda create-function \
#   --function-name abstractabstraction-api \
#   --runtime python3.13 \
#   --zip-file fileb://package.zip \
#   --handler main.handler \
