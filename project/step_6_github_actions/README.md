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
          echo "🎬 The job was automatically triggered by a ${{ github.event_name }} event."
          echo "💻 This job is now running on a ${{ runner.os }} server hosted by GitHub!"
          echo "🎋 Workflow is running on the branch ${{ github.ref }}"
      - name: Checking out the repository
        uses: actions/checkout@v2
      - name: Information after checking out
        run: |
          echo "💡 The ${{ github.repository }} repository has been cloned to the runner."
          echo "🖥️ The workflow is now ready to test your code on the runner."
      - name: List files in the repository
        run: |
          ls ${{ github.workspace }}
      - run: echo "🍏 This job's status is ${{ job.status }}."
```
- `on` is called an event which triggers the workflow. Here it is push event. Whenever a push is happened on the repository, workflow will be triggered. There are [many ways](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows) of triggering the workflow.
- Checking out the repository step contains the action to checkout the repository. Here we are using actions/checkoutv2 which is a [open source action](https://github.com/marketplace?type=actions).
- Add this file and push it to GitHub, then move to the online repository and you should be able to see the workflow running under the tab `Actions`.
***

## References
- [Blog post](https://www.ravirajag.dev/blog/mlops-github-actions)
- [GitHub code](https://github.com/graviraja/MLOps-Basics/tree/main/week_6_github_actions)
- [Main GitHub project page](https://github.com/graviraja/MLOps-Basics)
- [From notebooks to productions pipelines](https://github.com/kyaiooiayk/CI-CD-Pipeline-with-GitHub-Actions)
- [Configuring service account](https://dvc.org/doc/user-guide/setup-google-drive-remote)
- [Github actions](https://docs.github.com/en/actions/quickstart)
***