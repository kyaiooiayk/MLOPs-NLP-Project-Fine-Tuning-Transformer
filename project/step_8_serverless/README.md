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

## References
- [Blog post](https://www.ravirajag.dev/blog/mlops-serverless)
- [GitHub code](https://github.com/graviraja/MLOps-Basics/tree/main/week_8_serverless)
- [Main GitHub project page](https://github.com/graviraja/MLOps-Basics)
- [An introduction to what AWS Lmbda function](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/AWS/AWS_Lambda)
***
