# ai-homework-9
This projects consists of 2 parts:
- `convert_to_lite.ipynb` notebook converts a dino-dragon model to a lite version so that it can be used with tflite runtime
- a `Dockerfile` that build a docker image compatible with AWS Lambda so that the model can be deployed as a serverless function

# Build and Deploy To AWS Lambda
To build and deploy the model as a serverless function, follow these steps:
1. Clone the repo
2. Edit `Makefile` variables
3. Configure AWS CLI
4. Log in to ECR by running `aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin xxxxx.dkr.ecr.us-east-1.amazonaws.com`. Replace region and `xxxxx.dkr.ecr.us-east-1.amazonaws.com` with your ECR repository URI
5. Run `make all` to build the docker image and push it to ECR
6. Create a new Lambda function and select the container image option using AWS console