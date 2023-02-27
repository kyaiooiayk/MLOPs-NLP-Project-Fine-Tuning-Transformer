# Step 5 - Model Packaging - Docker 
- [ ] Step #0: Project Setup
- [ ] Step #1: Model monitoring - Weights and Biases
- [ ] Step #2: Configurations - Hydra
- [ ] Step #3: Data Version Control - DVC
- [ ] Step #4: Model Serialisation - ONNX
- [x] Step #5: Model Packaging - Docker
- [ ] Step #6: CI/CD - GitHub Actions
- [ ] Step #7: Container Registry - AWS ECR
- [ ] Step #8: Serverless Deployment - AWS Lambda
- [ ] Step #9: Prediction Monitoring - Kibana
***

## Virtual environment setup
- If you have your virtual environment created in step #0 active you are set to go, if not activate it with: `conda activate mlops`
- Install these additional packages:
    - `pip install fastapi`
    - `pip install uvicorn`
- Follow [this instructions](https://github.com/kyaiooiayk/Docker-Notes#installation) to install docker.
- Write a `requirements.txt` fie with `pipreqs --savepath=requirements.in && pip-compile --resolver=backtracking`. If you want to know more about this last command see [here](https://github.com/kyaiooiayk/Python-Programming/blob/main/tutorials/requirements.md)
- If anyone else would like to follow what you have done all they need to do is: `pip install -r requirements.txt`
***

## Programming best prectices
- Install `black` linter on MacOS system: `brew install black`
- Install `flake8` linter on a MacOS system: `brew install black`
- Start black on MacOS with: `brew services start black`.
- Use `black name_of_your_python_script.py` which will automatically reformat the code for you.
- Use `flake8 name_of_your_python_script.py` to have see if any suggestion about code formatting is printed on screen.
- Write a `requirements.txt` fie with `pipreqs --savepath=requirements.in && pip-compile --resolver=backtracking`. If you want to know more about this last command see [here](https://github.com/kyaiooiayk/Python-Programming/blob/main/tutorials/requirements.md)
- If anyone else would like to follow what you have done all they need to do is: `pip install -r requirements.txt`
***

## FastAPI
- What if you want to integrate your machine learning model into a larger software solution instead of a simple standalone web application?
- What if you are working alongside a software engineer who is building a large application and needs to access your model through a REST API? This exactly where FastAPI comes into play.
- FastAPI is a Python web framework that makes it easy for developers to build fast (high-performance), production-ready REST APIs. If you’re a data scientist who works mostly with Python, FastAPI is an excellent tool for deploying your models as REST APIs. 
- FastAPI is based on Pydantic and type hints to validate, serialise, and deserialise data, and automatically auto-generate OpenAPI documents. 
- It fully supports asynchronous programming and can run with `Uvicorn` and `Gunicorn`. 
- [FastAPI vs. Django vs. Falsk](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/FastAPI)
***

## Create an app with FastAPI
- Create a file called `app.py` where we are going to add:
    - An API whick will take the user to an home page
    - An API which will take text as input and returns the prediction.
```python
from fastapi import FastAPI
from inference_onnx import ColaONNXPredictor
app = FastAPI(title="MLOps Basics App")

predictor = ColaONNXPredictor("./models/model.onnx")

@app.get("/")
async def home_page():
    return "<h2>Sample prediction API</h2>"


@app.get("/predict")
async def get_prediction(text: str):
    result =  predictor.predict(text)
    return result
```
- Run the application using the command: `uvicorn app:app --ip 0.0.0.0 --port 8000 --reload`
- Copy and past the following on your browser: http://localhost:8000/

![image](https://user-images.githubusercontent.com/89139139/221551082-5bbea947-f556-4295-b496-1b6cc609b320.png)
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

## Create a Docker file
- A Docker file is a file where a series of instructions are written in order to build a Docker Image. Each instruction in a docker file is a command/operation, for example, what operating system to use, what dependencies to install or how to compile the code, and many such instructions which act as a **layer**.
- Each line which represents a layers is cached and if we modified some instructions in the Dockerfile then during the build process it will just rebuild the changed layer. Building an image can take some time, so caching is a good way to avoid repeating the same operation.
- Create a file `Dockerfile` with the following content:
```shell
FROM huggingface/transformers-pytorch-cpu:latest
COPY ./ /app
WORKDIR /app
RUN pip install -r requirements_inference.txt
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```
***

## How to build the docker image
- Build the image using the command: `docker build -t inference:latest .`
- Then run the container using the command: `docker run -p 8000:8000 --name inference_container inference:latest`
***

## Docker composer
- Docker Compose is a tool that was developed to help define and share multi-container applications. With Compose, we can create a YAML file to define the services and with a single command, can spin everything up or tear it all down.
- The key difference between `docker` run versus `docker-compose` is that docker run is entirely command line based, while docker-compose reads configuration data from a `YAML` file. The second major difference is that docker run can only start one container at a time, while docker-compose will configure and run multiple.
- As cloud-native environments increase in complexity, docker run commands will become unmanageable long. When a docker run command becomes more than seventy or eighty characters in length, it makes more sense to configure the container in a docker-compose.yaml file.

## Seeting up a YMAL Docker compose file
Let's see how to create a compose yaml file called `docker-compose.yml`:
```shell
version: '3'
services:
  prediction_api:
    build: .
    container_name: 'inference_container'
    ports:
      - '8000:8000'
```
- `services` is where you list all your container, in our case there is only one.
- Build and run the container using the command: `docker-compose up`
***

## Docker sharing
- Sharing can be done in 2 ways:
    - Commit the Dockerfile which can be used to build the image and container
    - Push the docker image to a central repository like Docker Hub and pull it from there. You need to create an account in docker hub in-order to be able to push the image.
***

## References
- [Blog post](https://www.ravirajag.dev/blog/mlops-docker)
- [GitHub code](https://github.com/graviraja/MLOps-Basics/tree/main/week_5_docker)
- [Main GitHub project page](https://github.com/graviraja/MLOps-Basics)
- [Analytics vidhya blog](https://www.analyticsvidhya.com/blog/2021/06/a-hands-on-guide-to-containerized-your-machine-learning-workflow-with-docker/)
- [FastAPI Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/FastAPI)
***
