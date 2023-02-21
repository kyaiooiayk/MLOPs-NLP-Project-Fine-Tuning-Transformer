# Week 3 - Data Version Control - DVC
- [ ] Week 0: Project Setup
- [ ] Week 1: Model monitoring - Weights and Biases
- [ ] Week 2: Configurations - Hydra
- [x] Week 3: Data Version Control - DVC
- [ ] Week 4: Model Serialisation - ONNX
- [ ] Week 5: Model Packaging - Docker
- [ ] Week 6: CI/CD - GitHub Actions
- [ ] Week 7: Container Registry - AWS ECR
- [ ] Week 8: Serverless Deployment - AWS Lambda
- [ ] Week 9: Prediction Monitoring - Kibana
***


## Virtual environment setup
- If you have your virtual environment created in week 0 active you are set to go, if not activate it with: `conda activate mlops`
- Install this additional package:
    - `pip install dvc`
- After these extra packages were installed, save the new requirements file with: `pip freeze -> requirements.txt`
***

## DVC
- DVC stands for Data Version Control and is open-source.
- Interact perfectly with Git and the combination Git/DVC is one of the most popular choice for simple versioning.
- DVC works by supplementing each data file with a corresponding metadata file (.dvc), which is used to sync with a remote repository designed for large files (All the large files, datasets, models, etc. can be stored in remote storage servers (S3, Google Drive, etc).
- DVC supports easy-to-use commands to configure, push, pull datasets to remote storage.).
- Git tracks the metadata file, while DVC handles the remote repository.
***

## References
- [Blog post](https://www.ravirajag.dev/blog/mlops-dvc)
- [GitHub code](https://github.com/graviraja/MLOps-Basics/tree/main/week_3_dvc)
- [Main GitHub project page](https://github.com/graviraja/MLOps-Basics)
***