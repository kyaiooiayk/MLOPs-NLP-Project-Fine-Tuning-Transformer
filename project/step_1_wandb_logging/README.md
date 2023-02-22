# Step 1 - Model monitoring - Weights and Biases
- [ ] Step #0: Project Setup
- [x] Step #1: Model monitoring - Weights and Biases
- [ ] Step #2: Configurations - Hydra
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
    - `pip install wandb`
    - `pip install torchmetrics`
    - `pip install matplotlib`
    - `pip inatall seaborn`
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

## Monitoring
- Experiment tracking/monitoring allows us to manage all the experiments along with their components, such as parameters, metrics, and more. It makes easier to track the evolution of your model as you learn more and more about the problem. Here are some available tools:
  - [MLFlow](https://mlflow.org/) is an open source project that offers experiment tracking and multiframe‐work support including Apache Spark, but limited workflow support. If you need a lightweight, simple way to track experiments and run simple workflows, this may be a good choice.
  - [Comet ML](https://www.comet.com/site/) 
  - [Neptune](https://neptune.ai/)
  - [Weights and Biases](https://wandb.ai/site) Used in this tutorial.
  - [TensorBoard](https://www.tensorflow.org/tensorboard) It was used in week 0, but will show how W&B is better.
***

## Weights and Bias Configuration
- Create an free accoount at [W&B](https://wandb.ai/site). This is free for public projects and 100GB storage.
- Once account is created, we need to loging locally: `wandb login`, then gollow the authorisation link and copy paste the api key.
- Create a project at W&B and then use the same name here. So that all the experiments will be logged into that project.
- Update the `logger` inside the `train.py` script so that all the logs will be tracked in W&B.:
```python
# previous week
tb_logger = pl.loggers.TensorBoardLogger("logs/", name="cola", version=1)

# this week
wandb_logger = WandbLogger(project="<your_project_name>", entity="<your_user_name>")

...

# previous week
logger=pl.loggers.TensorBoardLogger("logs/", name="cola", version=1),
# this week
logger=wandb_logger
```
***
- The content of this folder is almost the same as what we have seen in week0 with the following differences:
    - `data.py` no changes
    - `train.py` changed and make sure you update the details realted to your W&B account
    - `inference.py` no change, but make sure to update the last saved checkpoint.
    - `model.py` changed especially the part related to the metrics.

## Re-train the model
- Yes, this step needs to be re-done even if you trained the model in week 0.
Once the training is completed in the end of the logs you will see something like:

```shell
wandb: Synced 5 W&B file(s), 4 media file(s), 3 artifact file(s) and 0 other file(s)
wandb: 
wandb: Synced proud-mountain-77: https://wandb.ai/<link_specific_to_yout_w_and_b_account>
```
- Follow the link to see the wandb dashboard which contains all the plots.
***

## Inference
- Once the model is trained, we can use the trained model to get predictions on the run time data.
- Typically Inference contains:
    - Load the trained model
    - Get the run time (inference) input
    - Convert the input in the required format
    - Get the predictions
- In the specific, go inside folder `./model/epoch=2-step=102.ckpt` and update the path inside the `inference.py` script.
- Run inference with: `python inference.py`
***

## References
- [Blog post](https://www.ravirajag.dev/blog/mlops-wandb-integration)
- [GitHub code](https://github.com/graviraja/MLOps-Basics/tree/main/week_1_wandb_logging)
- [Main GitHub project page](https://github.com/graviraja/MLOps-Basics)
- [Weights and Biases](https://wandb.ai/site)
- [torchmetrics](https://torchmetrics.readthedocs.io/)
- [Tutorial on Pytorch Lightning + Weights & Bias](https://www.youtube.com/watch?v=hUXQm46TAKc)
- [WandB Documentation](https://docs.wandb.ai/)
***