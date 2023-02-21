
# Step #0 - Project setup

- [x] Step #0: Project Setup
- [ ] Step #1: Model monitoring - Weights and Biases
- [ ] Step #2: Configurations - Hydra
- [ ] Step #3: Data Version Control - DVC
- [ ] Step #4: Model Serialisation - ONNX
- [ ] Step #5: Model Packaging - Docker
- [ ] Step #6: CI/CD - GitHub Actions
- [ ] Step #7: Container Registry - AWS ECR
- [ ] Step #8: Serverless Deployment - AWS Lambda
- [ ] Step #9: Prediction Monitoring - Kibana
***

## Creating a virtual environment
- Create a virtual env with the following command: `conda create --name MLOPS python=3.8.16`
- Activate the virtual environment: `conda activate MLOPS`
***

## Virtual environment setup
- Install the Huggingface datasets: `pip install datasets`
- Install the Huggingface LLM packages: `pip install transformers`
- Install PT lightening: `pip install pytorch_lightning`
- Install `black` linter on MacOS system: `brew install black`
- Install `flake8` linter on a MacOS system: `brew install black`
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
- The CoLA (Corpus of Linguistic Acceptability) dataset is about given a sentence it has to be classified into one of the two classes: 
    - Unacceptable if grammatically not correct
    - Acceptable if grammatically correct
- The dataset is donwload via the [HugginFace datasets](https://huggingface.co/docs/datasets/index) module for convenience.
***

## Jupyter notebook analysis
- The `data_exploration.ipynb` is used to quickly explore the dataset.
- Some more EDA could have been done here to be honest. I will leave it for the future.
***

## Lintering your code
- Start black on MacOS with: `brew services start black`. This will automatically reformat the code for you.
- Use `flake8 name_of_your_python_script.py` to have see if any suggestion about code formatting is printed on screen.
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
```python
class ColaModel(pl.LightningModule):
    def __init__(self, model_name="google/bert_uncased_L-2_H-128_A-2", lr=1e-2):
        super(ColaModel, self).__init__()
        self.save_hyperparameters()
        
        # We have two classes only
        self.num_classes = 2
            
        # Loading the pre-trained model
        self.bert = AutoModel.from_pretrained(model_name)
        
        # Adding one last layer which needs to be trained against 2 classes
        self.W = nn.Linear(self.bert.config.hidden_size, self.num_classes)


    def forward(self, input_ids, attention_mask):
        outputs = self.bert(input_ids=input_ids, attention_mask=attention_mask)

        h_cls = outputs.last_hidden_state[:, 0]
        logits = self.W(h_cls)
        return logits
```
- The number of params of the pre-trained model vs the number of parameter in the last layer we are fine tuning can be seen below:
```shell
  | Name | Type      | Params
-----------------------------------
0 | bert | BertModel | 4.4 M 
1 | W    | Linear    | 258   
-----------------------------------
```
***

## Training - `train.py`
- The `data.py` housing the DataLoader and the `model.py` housing the LightningModule are brought together inside the `train.py` script where a Trainer is defined.
- This orchestrates data loading, gradient calculation, optimiser, half precision, distributed computing and logging.
- I have personally run this tutorial on macbook pro with 12 cores and it tooks something arounf 1 hr to complete.
- Before you train your model, if you running it locally on your Mac check the limit of the maximum number of allowed open file with: `ulimit -a` and set to `ulimit -Sn 10000`, otherwise it will throw you an error. If it does, you can always restart the training from the last saved check point.
- To train the model: `python train.py`.
***

## Taining time on CPUs and GPUs
- On my MacBook Pro with 12 CPUs with batch_size=265 and epoches=3, it took 45 minutes
- On Google Colab on a single K80 batch_size=32 (pay attention to the GPU memory is not infinite!) and epoches=3 it took 5 minutes.
- If you are interest to know how to conncet you code on GitHub and Google Colab, see [here](https://github.com/kyaiooiayk/Awesome-LLM-Large-Language-Models-Notes). In short, 
    - The easiest option would be for you to clone this repository.
    - Navigate to Google Colab and open the notebook directly from Colab.
    - You can then also write it back to GitHub provided permission to Colab is granted. The whole procedure is automated.
***

## Logging
 This will create a directory called `logs/cola` if not present.
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
- In the specific, go inside folder `./model/` and look for the name of the checkpoint last save, in my case it was `epoch=2-step=102.ckpt`. Copy this value and paste it inside the `inference.py` script.
- Run inference with: `python inference.py`
- Here I testeed it for two sentences:
```python
if __name__ == "__main__":
    print("**********")
    print("Example #1")
    sentence = "The boy is sitting on a bench"
    predictor = ColaPredictor("./models/epoch=2-step=102.ckpt")
    print(predictor.predict(sentence))

    print("**********")
    print("Example #2")
    sentence = "They not yelled us!"
    predictor = ColaPredictor("./models/epoch=2-step=102.ckpt")
    print(predictor.predict(sentence))
```
***

## References
- [Blog post](https://www.ravirajag.dev/blog/mlops-project-setup-part1)
- [GitHub code](https://github.com/graviraja/MLOps-Basics/tree/main/week_0_project_setup)
- [Main GitHub project page](https://github.com/graviraja/MLOps-Basics)
- [Huggingface Datasets](https://github.com/huggingface/datasets)
- [Huggingface Transformers](https://github.com/huggingface/transformers)
- [Pytorch Lightning](https://pytorch-lightning.readthedocs.io/)
***
