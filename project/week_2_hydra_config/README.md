# Week 2 - Configurations - Hydra
- [ ] Week 0: Project Setup
- [ ] Week 1: Model monitoring - Weights and Biases
- [x] Week 2: Configurations - Hydra
- [ ] Week 3: Data Version Control - DVC
- [ ] Week 4: Model Serialisation - ONNX
- [ ] Week 5: Model Packaging - Docker
- [ ] Week 6: CI/CD - GitHub Actions
- [ ] Week 7: Container Registry - AWS ECR
- [ ] Week 8: Serverless Deployment - AWS Lambda
- [ ] Week 9: Prediction Monitoring - Kibana
***


## Virtual environment setup
- If you have your virtual environment created in week 0 active you are set to go, if not activate it with: `conda activate mlops`
- Install these additional packages:
    - `pip install hydra-core`
    - `pip install omegaconf`
    - `pip install hydra_colorlog`
- After these extra packages were installed, save the new requirements file with: `pip freeze -> requirements.txt`
***


## Hydra
- Hydra operates on top of OmegaConf, which is a YAML based hierarchical configuration system, with support for merging configurations from multiple sources (files, CLI argument, environment variables) providing a consistent API regardless of how the configuration was created.
***

## Hydra configurations
- Let's convert all the parameters in the existing code into yaml format and load it using hydra.
- In real scenarios there could be lot of modules and each module may have many parameters. Having all those parameters in a single file can look messy. Hydra offers a way to have configurations in multiple files and can be tied together via configuration groups
- Create a folder called `./configs`
- Create a file called `config.yaml`:
```shell
defaults:
  - model: default
  - processing: default
  - training: default
  - override hydra/job_logging: colorlog
  - override hydra/hydra_logging: colorlog
```
- For instance the first line tells hydra to look for folder model where a file called `default.yaml` is:
```shell
name: google/bert_uncased_L-2_H-128_A-2             # model used for training the classifier
tokenizer: google/bert_uncased_L-2_H-128_A-2        # tokenizer used for processing the data
```
***

## References
- [Blog post](https://www.ravirajag.dev/blog/mlops-hydra-config)
- [GitHub code](https://github.com/graviraja/MLOps-Basics/tree/main/week_2_hydra_config)
- [Main GitHub project page](https://github.com/graviraja/MLOps-Basics)
