# Week 5 - Model Packaging - Docker 
- [ ] Week 0: Project Setup
- [ ] Week 1: Model monitoring - Weights and Biases
- [ ] Week 2: Configurations - Hydra
- [ ] Week 3: Data Version Control - DVC
- [ ] Week 4: Model Serialisation - ONNX
- [x] Week 5: Model Packaging - Docker
- [ ] Week 6: CI/CD - GitHub Actions
- [ ] Week 7: Container Registry - AWS ECR
- [ ] Week 8: Serverless Deployment - AWS Lambda
- [ ] Week 9: Prediction Monitoring - Kibana
***


## Virtual environment setup
- If you have your virtual environment created in week 0 active you are set to go, if not activate it with: `conda activate mlops`
- Install these additional packages:
    - `pip install fastapi`
    - `pip install uvicorn`
- After these extra packages were installed, save the new requirements file with: `pip freeze -> requirements.txt`
- To install Docker on your machine follow this [link](https://github.com/kyaiooiayk/Docker-Notes).
***

## Docker
- Docker is a tool designed to create, deploy, and run applications by using containers. The applications you build, if shipped with a docker image, become reproducible anywhere. Containerisation offers a consistent state across different servers or cloud environments.
- It is open-source and essentially a container file format. It automates the deployment of applications as portable, self-sufficient containers that can run in the cloud or on-premises.
- A container is a standardized software unit, in simple terms — nothing but a packaged bundle of application code and required libraries and other dependencies.
- A Docker Image is an executable software package that includes everything needed to run an application and becomes a Container at runtime.
- Docker is like a virtual machine!
- It has its own filesystem and the files from your local machine are not shared to the docker container.
- If you want to use a path from your local machine and want to modify it too, you would need to mount it to the docker container when running it.
***

## Docker file vs. Docker image vs. Docker instance
- A **Docker File** contains the list of commands to run which are necessary for the application to run (like dependencies, codes, command to run etc.)
- A Docker Image** is a lightweight, standalone, executable package of software (built using dockerfile) that includes everything needed to run an application: code, runtime, system tools, system libraries, and settings.
- A **Docker Container** is an instance of Docker Image which contains the running application.
***

## FastAPI
- What if you want to integrate your machine learning model into a larger software solution instead of a simple standalone web application?
- What if you are working alongside a software engineer who is building a large application and needs to access your model through a REST API? This exactly where FastAPI comes into play.
- FastAPI is a Python web framework that makes it easy for developers to build fast (high-performance), production-ready REST APIs. If you’re a data scientist who works mostly with Python, FastAPI is an excellent tool for deploying your models as REST APIs. 
- FastAPI is based on Pydantic and type hints to validate, serialise, and deserialise data, and automatically auto-generate OpenAPI documents. 
- It fully supports asynchronous programming and can run with `Uvicorn` and `Gunicorn`. 
***

## How to build the docker image
- Build the image using the command: `docker build -t inference:latest .`
- Then run the container using the command: `docker run -p 8000:8000 --name inference_container inference:latest`
- Alternatively, build and run the container using the command: `docker-compose up`
***

## References
- [Blog post](https://www.ravirajag.dev/blog/mlops-docker)
- [GitHub code](https://github.com/graviraja/MLOps-Basics/tree/main/week_5_docker)
- [Main GitHub project page](https://github.com/graviraja/MLOps-Basics)
***
