# E2E NLP MLOps
***

## Introduction
- The goal of this project is to implement a semi-complex initial E2E project better described as E2E MLOps.
- Most of the scripts presented here are taken from this fantastic 8-week course called [MLOps-Basics](https://github.com/graviraja/MLOps-Basics) but are heavily modified, especially on their `README.md` files.
- This project will cover the full MLOps cycle. We'll implement an NLP model based on a pre-trained transformer achitecture which will be be fined-tuned, deployed and ultimately served.

<p align="center">
<img width="512" alt="image" src="https://user-images.githubusercontent.com/89139139/220432027-bf2df07b-bee8-4263-aa12-81e7236e338e.png">
<p>

***

## How to use this 9-step tutorials
- Each step build on top of the previous one.
- Do not assume that, just because files have the same name, they would have the same content.
***

## [Step #0: Project Setup](https://github.com/kyaiooiayk/MLOPs-NLP-Project-Fine-Tuning-Transformer/tree/main/project/step_0_project_setup)
- How to get the data?
- How to process the data?
- How to define  a `DataModules` in ⚡ Pytorch Lightning as opposed to the Vanilla Pytorch `DataLoaders`
- How to build a model to fine tune a pre-trained transformer on a classification task?
- How to train the model on both CPUs on your local machine or GPU on GoogleColab?
- How to do the inference?
***

## [Step #1: Model monitoring - Weights and Biases](https://github.com/kyaiooiayk/MLOPs-NLP-Project-Fine-Tuning-Transformer/tree/main/project/step_1_wandb_logging)
- How to configure basic logging with W&B?
- How to compute metrics and log them in W&B?
- How to add plots in W&B?
- How to add data samples to W&B?
***

## [Step #2: Configurations - Hydra](https://github.com/kyaiooiayk/MLOPs-NLP-Project-Fine-Tuning-Transformer/tree/main/project/step_2_hydra_config)
- Basics of Hydra and how is this different than a simple YMAL file
- Overridding configurations at run time
- Splitting configuration across multiple files
***

## [Step #3: Data Version Control - DVC](https://github.com/kyaiooiayk/MLOPs-NLP-Project-Fine-Tuning-Transformer/tree/main/project/step_3_dvc)
- Basics of DVC
- How DVC is similar to Git
- Initialising DVC
- Configuring Remote Storage
- Saving Model to the Remote Storage
- Versioning the models
***

## [Step #4: Model Packaging - ONNX](https://github.com/kyaiooiayk/MLOPs-NLP-Project-Fine-Tuning-Transformer/tree/main/project/step_4_onnx)
- Why do we need model packaging?
- What is ONNX?
- How to convert a trained model to ONNX format?`
- What is ONNX Runtime?
- How to run ONNX converted model in ONNX Runtime?
***

## [Step #5: Model Packaging - Docker](https://github.com/kyaiooiayk/MLOPs-NLP-Project-Fine-Tuning-Transformer/tree/main/project/step_5_docker)
- FastAPI wrapper
- How to create an app with FastAPI
- Basics of Docker
- Building Docker Container
- Docker Compose
***

## [Step #6: CI/CD - GitHub Actions](https://github.com/kyaiooiayk/MLOPs-NLP-Project-Fine-Tuning-Transformer/blob/main/project/step_6_github_actions/README.md)
- Basics of GitHub Actions
- First GitHub Action
- Creating Google Service Account
- Giving access to Service account
- Configuring DVC to use Google Service account
- Configuring Github Action
***

## [Step #7: Container Registry - AWS ECR](https://github.com/kyaiooiayk/MLOPs-NLP-Project-Fine-Tuning-Transformer/tree/main/project/step_7_ecr)
- Container registry 
- Basics of S3
- Programmatic access to S3
- Configuring AWS S3 as remote storage in DVC
- Basics of ECR
- Differences btw AWS S3 and AWS ECR
- Configuring GitHub Actions to use S3, ECR
***

## [Step #8: Serverless Deployment - AWS Lambda](https://github.com/kyaiooiayk/MLOPs-NLP-Project-Fine-Tuning-Transformer/tree/main/project/step_8_serverless)
- Basics of Serverless
- Basics of AWS Lambda
- Triggering Lambda with API Gateway
- Deploying Container using Lambda
- Automating deployment to Lambda using Github Actions
***


## Step #9: Prediction Monitoring - Kibana

<img src="https://img.shields.io/static/v1.svg?style=for-the-badge&label=difficulty&message=medium&color=orange"/>

Refer to the [Blog Post here](https://www.ravirajag.dev/blog/mlops-monitoring)


Monitoring systems can help give us confidence that our systems are running smoothly and, in the event of a system failure, can quickly provide appropriate context when diagnosing the root cause.

Things we want to monitor during and training and inference are different. During training we are concered about whether the loss is decreasing or not, whether the model is overfitting, etc.

But, during inference, We like to have confidence that our model is making correct predictions.

There are many reasons why a model can fail to make useful predictions:

- The underlying data distribution has shifted over time and the model has gone stale. i.e inference data characteristics is different from the data characteristics used to train the model.

- The inference data stream contains edge cases (not seen during model training). In this scenarios model might perform poorly or can lead to errors.

- The model was misconfigured in its production deployment. (Configuration issues are common)

In all of these scenarios, the model could still make a `successful` prediction from a service perspective, but the predictions will likely not be useful. Monitoring machine learning models can help us detect such scenarios and intervene (e.g. trigger a model retraining/deployment pipeline).

In this week, I will be going through the following topics:

- `Basics of Cloudwatch Logs`

- `Creating Elastic Search Cluster`

- `Configuring Cloudwatch Logs with Elastic Search`

- `Creating Index Patterns in Kibana`

- `Creating Kibana Visualisations`

- `Creating Kibana Dashboard`

![Docker](images/kibana_flow.png)

## Refernces
- [Main GitHub project page](https://github.com/graviraja/MLOps-Basics)
***
