# Step 8 - Serverless Deployment - AWS Lambda
- [ ] Step #0: Project Setup
- [ ] Step #1: Model monitoring - Weights and Biases
- [ ] Step #2: Configurations - Hydra
- [ ] Step #3: Data Version Control - DVC
- [ ] Step #4: Model Serialisation - ONNX
- [ ] Step #5: Model Packaging - Docker
- [ ] Step #6: CI/CD - GitHub Actions
- [ ] Step #7: Container Registry - AWS ECR
- [x] Step #8: Serverless Deployment - AWS Lambda
- [ ] Step #9: Prediction Monitoring - Kibana
***

## Virtual environment setup
- If you have your virtual environment created in step #0 active you are set to go, if not activate it with: `conda activate mlops`
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

## Serveless deployment
- A serverless architecture is a way to build and run applications and services without having to manage infrastructure. The application still runs on servers, but all the server management is done by third party service. We no longer have to provision, scale, and maintain servers to run the applications, databases, and storage systems.
- There are at least 3 providers:
    - [Google Cloud Functions](https://cloud.google.com/functions/)
    - [Azure Functions](https://azure.microsoft.com/en-us/products/functions/)
    - [IMB Cloud Functions](https://www.ibm.com/cloud/functions)
    - AWS Lambda functions | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/AWS/AWS_Lambda).
***

## Pros & cons
- **Pros**
    - It abstracts away the server details and lets you serve your code or model with few lines of code
    - It will handle the provising of servers
    - It will scale the machines up and down depending on usage
    - Does the load balancing
    - No cost when the code is not running
- **Cons**
    - Response latency: Since the code is not running readily and will only run once it is called, there will be latency till the code is up and running
    - Not useful for long running processes: Serverless providers charge for the amount of time code is running, it may cost more to run an application with long-running processes in a serverless infrastructure compared to a traditional one.
    - Difficult to debug: Debugging is difficult since the developer cannot have the access(ssh) to the machine where the code is running.
    - Vendor limitations: Setting up a serverless architecture with one vendor can make it difficult to switch vendors if necessary, especially since each vendor offers slightly different features and workflows.
***

## Setting up a AWS Lambda function
- Sign into your `AWS Management Console` and search for `Amazon Lambda`.
- Click on `Create Function` 
![image](https://user-images.githubusercontent.com/89139139/222493174-a9c84178-80c0-4461-abf8-f7736c3bc8c3.png)
- Fill in `function name` and choose python for the `runtime` type
![image](https://user-images.githubusercontent.com/89139139/222493464-bbd250d5-c91d-4a71-b4f8-1b326bd675d8.png)
- Click on `Test` button
![image](https://user-images.githubusercontent.com/89139139/222493982-e89e5515-5620-40c0-9627-c4fc86605c2f.png)
***

## Triggering Lambda with API Gateway
- How do we call/trigger a lambda function? There are different ways to trigger the lambda. Let's see how to do it using API Gateway.
- API Gateway handles all the tasks involved in accepting and processing up to hundreds of thousands of concurrent API calls, including traffic management, CORS support, authorization and access control, throttling, monitoring, and API version management.
- On your `AWS Management Console` search for the `Amazon API Gateway` and click on `Build` button under `HTTP API`
![image](https://user-images.githubusercontent.com/89139139/222496950-c2be3520-442a-4390-b4e6-75f2c5f0d7c5.png)
- Fill in the `Integration` and the `Lambda function` boxes:
![image](https://user-images.githubusercontent.com/89139139/222497241-e7f067d2-cc21-438e-98cc-b9fe10f5f793.png)
- Upon refreshing the page you shouldbe abel to see `API Gateway` and under `Configuration` click on `API endpoint` to verify it is up and running: 
![image](https://user-images.githubusercontent.com/89139139/222498097-065640d8-1eb8-4d6b-86b8-04e90b5cc843.png)
***

## Deploying Container using Lambda
- How do we deploy the container thar is persisting in the ECR bucket?
- Create a new lambda function with name MLOps-Basics and choose the type as `Container Image`
![image](https://user-images.githubusercontent.com/89139139/222512310-d046a822-425a-438e-bb79-6f4f36e54905.png)
- Since the model size is more than 100MB and it will take some time to load, go the `Configuration` section and update the memory size and timeout
![image](https://user-images.githubusercontent.com/89139139/222512821-8a80c829-cfee-46b8-b772-c5f9bdbfc98e.png)
- Now let's configure the `Test` so that the lambda can be tested. Go to the `Test` section and configure the test event:
![image](https://user-images.githubusercontent.com/89139139/222512926-632b6695-7aea-4db7-a6c1-2adef534b96f.png)
- Create a file called `lambda_handler.py` in the root directory. The contents of the file are as follows:
```python
import json
from inference_onnx import ColaONNXPredictor

inferencing_instance = ColaONNXPredictor("./models/model.onnx")

def lambda_handler(event, context):
    """
    Lambda function handler for predicting linguistic acceptability of the given sentence
    """

    if "resource" in event.keys():
        body = event["body"]
        body = json.loads(body)
        ...
```
- When the lambda function is triggered with API it recevies some information regarding the request. A sample looks like the following:
```json
{
  "resource": "/prediction",
  "path": "/prediction",
  "httpMethod": "POST",
  "headers": {
    "Accept": "*/*",
    ....
    ....
  "body": "{\n    \"sentence\": \"this is a sample sentence\"\n}",
  "isBase64Encoded": False
}
```
- Since the input for the model is under `body`, the `lambda_handler.py` is essentially a parser that retrieve that information.
- Our `Dockerfile` needs some updates as well:
```
FROM amazon/aws-lambda-python

ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG MODEL_DIR=./models
RUN mkdir $MODEL_DIR

ENV TRANSFORMERS_CACHE=$MODEL_DIR \
    TRANSFORMERS_VERBOSITY=error

ENV AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
    AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY

RUN yum install git -y && yum -y install gcc-c++
COPY requirements_inference.txt requirements_inference.txt
RUN pip install -r requirements_inference.txt --no-cache-dir
COPY ./ ./
ENV PYTHONPATH "${PYTHONPATH}:./"
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
RUN pip install "dvc[s3]"
# configuring remote server in dvc
RUN dvc init --no-scm
RUN dvc remote add -d model-store s3://models-dvc/trained_models/

# pulling the trained model
RUN dvc pull dvcfiles/trained_model.dvc

RUN python lambda_handler.py
RUN chmod -R 0755 $MODEL_DIR
CMD [ "lambda_handler.lambda_handler"]
```
- Here are the changes:
    - Changed the base image to `amazon/aws-lambda-python`
    - Added the Transformers cache directory as `models`
    - Added a sample run python `lambda_handler.py`. This will download the tokenizer required and saves it in the cache.
    - Given permissions to the models directory
    - Modified the default CMD to run as `lambda_handler.lambda_handler`
***

## References
- [Blog post](https://www.ravirajag.dev/blog/mlops-serverless)
- [GitHub code](https://github.com/graviraja/MLOps-Basics/tree/main/week_8_serverless)
- [Main GitHub project page](https://github.com/graviraja/MLOps-Basics)
- [An introduction to what AWS Lmbda function](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/AWS/AWS_Lambda)
***
