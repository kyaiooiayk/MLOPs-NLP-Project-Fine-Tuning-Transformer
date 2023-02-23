# Steep 2 - Configurations - Hydra
- [ ] Step #0: Project Setup
- [ ] Step #1: Model monitoring - Weights and Biases
- [x] Step #2: Configurations - Hydra
- [ ] Step #3: Data Version Control - DVC
- [ ] Step #4: Model Serialisation - ONNX
- [ ] Step #5: Model Packaging - Docker
- [ ] Step #6: CI/CD - GitHub Actions
- [ ] Step #7: Container Registry - AWS ECR
- [ ] Step #8: Serverless Deployment - AWS Lambda
- [ ] Step #9: Prediction Monitoring - Kibana
***


## Virtual environment setup
- If you have your virtual environment created in step #0 active you are set to go, if not activate it with: `conda activate mlops`
- Install these additional packages:
    - `pip install hydra-core`
    - `pip install omegaconf`
    - `pip install hydra_colorlog`
- After these extra packages were installed, save the new requirements file with: `pip freeze -> requirements.txt`
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

## Hydra
- Hydra is a configuration management used for managing complex software systems. 
- Hydra operates on top of `OmegaConf`, which is a YAML based hierarchical configuration system, with support for merging configurations from multiple sources (files, CLI argument, environment variables) providing a consistent API regardless of how the configuration was created.
***

## An example of how Hydra is different from a simple YAML file

- Let's create a `config.yaml`:

```ymal
preferences:
  user: raviraja
  trait: i_like_my_sleeping
```

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
- [Hydra](https://hydra.cc/)
- [Hydra Documentation](https://hydra.cc/docs/intro)
- [Simone Tutorial on Hydra](https://www.sscardapane.it/tutorials/hydra-tutorial/#executing-multiple-runs)
***