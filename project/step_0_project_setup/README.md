
# Week 0 - Project setup

- [x] Step 0: Project Setup
- [ ] Step 1: Model monitoring - Weights and Biases
- [ ] Step 2: Configurations - Hydra
- [ ] Step 3: Data Version Control - DVC
- [ ] Step 4: Model Serialisation - ONNX
- [ ] Step 5: Model Packaging - Docker
- [ ] Step 6: CI/CD - GitHub Actions
- [ ] Step 7: Container Registry - AWS ECR
- [ ] Step 8: Serverless Deployment - AWS Lambda
- [ ] Step 9: Prediction Monitoring - Kibana
***

## Creating a virtual environment
- Create a virtual env with the following command: `conda create --name MLOPS python=3.8.16`
- Activate the virtual environment: `conda activate MLOPS`
***

## Virtual environment setup
- Install the Huggingface datasets: `pip install datasets`
- Install the Huggingface LLM packages: `pip install transformers`
- Install PT lightening: `pytorch_lightning`
- Dump the current installed packages: `pip freeze > requirements.txt`. If anyone else would like to follow what you have done all the need to do is: `pip install -r requirements.txt`
***

## Setting up jupyter notebook
- Install jupyte notebook `pip install jupyter`
- To maker sure the new virtual environment is available in your drop down kernel options follows the following steps:
    - Install ipykernel: `conda install -c anaconda ipykernel`
    - Add your new virtual environment to ipykernel: `python -m ipykernel install --user --name=mlops`
- If you like to have access to all the jupyter notebook extenstions (although this is not necesary): `pip install jupyter_contrib_nbextensions && jupyter contrib nbextension install`
- If you want to know more read [this](https://github.com/kyaiooiayk/Jupyter-Notebooks)
***

## Dataset
- The CoLA (Corpus of Linguistic Acceptability) dataset is about given a sentence it has to be classified into one of the two classes: unacceptable if grammatically not correct or acceptable if grammatically correct.
***


## Jupyter notebook analysis
- The `data_exploration.ipynb` is used to quickly explore the dataset.
- Some more EDA could have been done here to be honest. I will leave it for the future.
***

## Loading the data - `data.py`
- Data pipelines can be created with:
    - Vanilla Pytorch `DataLoaders`: lower level and allow a lot of customisation
    - Pytorch Lightning `DataModules`: higher level and take, and should be used when possible (used here)
- A DataModule encapsulates the five steps involved in data processing in PyTorch:
    - Download / tokenize / process.
    - Clean and (maybe) save to disk.
    - Load inside Dataset.
    - Apply transforms (rotate, tokenize, etc…).
    - Wrap inside a DataLoader. 
***

## Modelling - `model.py`
- In PyTorch Lightning, models are built with LightningModule, which has all the functionality of a vanilla torch.nn.Module which helps you cut down on boilerplate and help separate out the ML engineering code from the actual machine learning.
- If you are interested in a line-by-line comparison btw vanilla and lightening please check [MLP in PyTorch and Lightning.ipynb](https://github.com/kyaiooiayk/PyTorch-Notes/blob/main/tutorials/MLP%20in%20PyTorch%20and%20Lightning.ipynb)
- Another important point to keep in mind here is that we are fine tuning a larger pre-trained model called: `google/bert_uncased_L-2_H-128_A-2` on a classification task having 2 classes.
***

## Training - `train.py`
- The `data.py` housing the DataLoader and the `model.py` housing the LightningModule are brought together inside the `train.py` script where a Trainer is defined.
- This orchestrates data loading, gradient calculation, optimiser, half precision, distributed computing and logging.
- I have personally run this tutorial on macbook pro with 12 cores and it tooks something arounf 1 hr to complete.
***

## Logging
- To train the model: `python train.py`. This will create a directory called `logs/cola` if not present.
- You can visualise the tensorboard logs using the following command: `tensorboard --logdir logs/cola` and to see the tensorboard at http://localhost:6006/.
- After training, update the model checkpoint path in the code and run: `python inference.py`
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
- [Blog post](https://www.ravirajag.dev/blog/mlops-project-setup-part1)
- [GitHub code](https://github.com/graviraja/MLOps-Basics/tree/main/week_0_project_setup)
- [Main GitHub project page](https://github.com/graviraja/MLOps-Basics)
- [Huggingface Datasets](https://github.com/huggingface/datasets)
- [Huggingface Transformers](https://github.com/huggingface/transformers)
- [Pytorch Lightning](https://pytorch-lightning.readthedocs.io/)
***
