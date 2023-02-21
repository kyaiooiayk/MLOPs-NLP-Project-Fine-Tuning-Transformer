# Week 6 - CI/CD - GitHub Actions
- [ ] Week 0: Project Setup
- [ ] Week 1: Model monitoring - Weights and Biases
- [ ] Week 2: Configurations - Hydra
- [ ] Week 3: Data Version Control - DVC
- [ ] Week 4: Model Serialisation - ONNX
- [ ] Week 5: Model Packaging - Docker
- [x] Week 6: CI/CD - GitHub Actions
- [ ] Week 7: Container Registry - AWS ECR
- [ ] Week 8: Serverless Deployment - AWS Lambda
- [ ] Week 9: Prediction Monitoring - Kibana
***

## Virtual environment setup
- If you have your virtual environment created in week 0 active you are set to go, if not activate it with: `conda activate mlops`
- No additional packages needs to be installed.
***

## GitHub Actions
- **CI/CD** is a coding philosophy and set of practices with which you can continuously build, test, and deploy iterative code changes.
- **CI** is about how the project should be built and tested in various runtimes, automatically and continuously. 
- **CD** is needed so that every new bit of code that passes automated testing can be released into production with no extra effort.
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

## References
- [Blog post](https://www.ravirajag.dev/blog/mlops-github-actions)
- [GitHub code](https://github.com/graviraja/MLOps-Basics/tree/main/week_6_github_actions)
- [Main GitHub project page](https://github.com/graviraja/MLOps-Basics)
- [From notebooks to productions pipelines](https://github.com/kyaiooiayk/CI-CD-Pipeline-with-GitHub-Actions)
***