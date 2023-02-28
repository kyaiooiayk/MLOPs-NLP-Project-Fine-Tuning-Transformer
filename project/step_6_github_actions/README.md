# Step 6 - CI/CD - GitHub Actions
- [ ] Step #0: Project Setup
- [ ] Step #1: Model monitoring - Weights and Biases
- [ ] Step #2: Configurations - Hydra
- [ ] Step #3: Data Version Control - DVC
- [ ] Step #4: Model Serialisation - ONNX
- [ ] Step #5: Model Packaging - Docker
- [x] Step #6: CI/CD - GitHub Actions
- [ ] Step #7: Container Registry - AWS ECR
- [ ] Step #8: Serverless Deployment - AWS Lambda
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

## Available tools
- **CI/CD** is a coding philosophy and set of practices with which you can continuously build, test, and deploy iterative code changes.
- **CI** is about how the project should be built and tested in various runtimes, automatically and continuously. 
- **CD** is needed so that every new bit of code that passes automated testing can be released into production with no extra effort.
- There are many tools with which we can perform CI/CD. The prominent ones are: Jenkins, CircleCI, Travis CI, GitLab, GitHub Actions. See [here](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/blob/master/README.md#cicd) for a comparison.
***

## GitHub Actions Intro
- If you are using GitHub to version control your code, you can use GitHub Actions right off the bat without having the need to setup another tool.
- GitHub Actions are just a set instructions declared using `yaml` files.
- These files needs to be in a specific folder: `.github/workflows` and this has to be in the root directory (where `.git` hidden folder is present).
- There are 5 main concepts in GitHub Actions:
    - **Event** which is an event that triggers for workflow.
    - **Job** defines the steps to run when a workflow is triggered. A workflow can contain multiple jobs.
    - **Runner** defines where to run the code. By default, github will run the code in it's own servers.
    - **Step** contains actions to run. Each job can contains multiple steps to run.
    - **Action** contains actual commands to run like installing dependencies, testing code, etc.
***

## How to create a GitHub workflow
- Create the folder using the command: `mkdir .github/workflows` with the followin content:
```shell
name: GitHub Actions Basic Flow
on: [push]
jobs:
  Basic-workflow:
    runs-on: ubuntu-latest
    steps:
      - name: Basic Information
        run: |
          echo "The job was automatically triggered by a ${{ github.event_name }} event."
          echo "This job is now running on a ${{ runner.os }} server hosted by GitHub!"
          echo "Workflow is running on the branch ${{ github.ref }}"
      - name: Checking out the repository
        uses: actions/checkout@v2
      - name: Information after checking out
        run: |
          echo "The ${{ github.repository }} repository has been cloned to the runner."
          echo "The workflow is now ready to test your code on the runner."
      - name: List files in the repository
        run: |
          ls ${{ github.workspace }}
      - run: echo "This job's status is ${{ job.status }}."
```
- `on` is called an event which triggers the workflow. Here it is push event. Whenever a push is happened on the repository, workflow will be triggered. There are [many ways](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows) of triggering the workflow.
- Checking out the repository step contains the action to checkout the repository. Here we are using actions/checkoutv2 which is a [open source action](https://github.com/marketplace?type=actions).
- Add this file and push it to GitHub, then move to the online repository and you should be able to see the workflow running under the tab `Actions`.

![image](https://user-images.githubusercontent.com/89139139/221843412-3ee4213f-9dad-4585-8c1f-9497742121d9.png)
- Now that service account is created, add this to the remote server (google drive). Go to the google drive and navigate to the remote storage folder (MLOps) and this service account email in the sharing permissions.
***

## Google service account
- In step #3 we have seen how we can out trained model checkpoint on GoogleDrive, but we have done all the authentification manually. To be able to it automatically inside a CI/CD pipeline we need to create a service account.
- A **service account** is a Google account associated with your GCP (Google Cloud Platform) project, and not a specific user.
- Go to [GCP console](https://cloud.google.com/cloud-console), sign-up or log-in depending on your case and create a project.
- To create a service account, navigate to IAM & Admin in the left sidebar, and select Service Accounts. Click + CREATE SERVICE ACCOUNT, on the next screen, enter Service account name e.g. "MLOps", and click Create.
![image](https://user-images.githubusercontent.com/89139139/221855484-7f894acb-8c3f-4188-b1e8-63ba46866ceb.png)
- Provide a name to service account like `model` and click `Done`
![image](https://user-images.githubusercontent.com/89139139/221855623-81f3e977-b3cc-4a52-a9f4-feda7c87dddd.png)
- Go the `keys` tab and create a new key. When prompted choose the key type as a `json` format. A json file will be downloaded and keep in mind this is supposed to remain secret.
![image](https://user-images.githubusercontent.com/89139139/221855761-0deca28d-e8b4-4bb8-8f7b-80659c387ca5.png)
- Search for `Google Drive API` in the search bar and enable it:
![image](https://user-images.githubusercontent.com/89139139/221856055-9de18c47-c51d-4ffe-86bd-c5b014e1ae50.png)
***

## Configuring DVC to use Google Service account
- Modify the DVC to use `service account` instead of actual google account as done in step #3. This can be done via:
```shell
dvc remote add -d storage gdrive://<your_alpha_numerical_code>
dvc remote modify storage gdrive_use_service_account true
dvc remote modify storage gdrive_service_account_json_file_path creds.json
```
- We can test it by trying to pull the model using the command:
```
cd dvcfiles
dvc pull trained_model.dvc
```
***

## Modify the Dockerfile
```shell
FROM huggingface/transformers-pytorch-cpu:latest

COPY ./ /app
WORKDIR /app

# install requirements
RUN pip install "dvc[gdrive]"
RUN pip install -r requirements_inference.txt

# initialise dvc
RUN dvc init --no-scm
# configuring remote server in dvc
RUN dvc remote add -d storage gdrive://19JK5AFbqOBlrFVwDHjTrf9uvQFtS0954
RUN dvc remote modify storage gdrive_use_service_account true
RUN dvc remote modify storage gdrive_service_account_json_file_path creds.json

# pulling the trained model
RUN dvc pull dvcfiles/trained_model.dvc

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# running the application
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```
***

## Create a new GitHubAction
- Now let's create a new github action file in `.github/worflows` folder as `build_docker_image.yaml` with the following content:
```
name: Create Docker Container

on: [push]

jobs:
  mlops-container:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: ./week_6_github_actions
    steps:
      - name: Checkout
        uses: actions/checkout@v2
        with:
          ref: ${{ github.ref }}
      - name: Build container
        run: |
          docker network create data
          docker build --tag inference:latest .
          docker run -d -p 8000:8000 --network data --name inference_container inference:latest
```
***

## References
- [Blog post](https://www.ravirajag.dev/blog/mlops-github-actions)
- [GitHub code](https://github.com/graviraja/MLOps-Basics/tree/main/week_6_github_actions)
- [Main GitHub project page](https://github.com/graviraja/MLOps-Basics)
- [From notebooks to productions pipelines](https://github.com/kyaiooiayk/CI-CD-Pipeline-with-GitHub-Actions)
- [Configuring service account](https://dvc.org/doc/user-guide/setup-google-drive-remote)
- [Github actions](https://docs.github.com/en/actions/quickstart)
***
