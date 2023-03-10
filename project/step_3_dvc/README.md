# Step 3 - Data Version Control - DVC
- [ ] Step #0: Project Setup
- [ ] Step #1: Model monitoring - Weights and Biases
- [ ] Step #2: Configurations - Hydra
- [x] Step #3: Data Version Control - DVC
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
    - `pip install dvc`
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

## DVC
- DVC stands for Data Version Control and is open-source.
- Interact perfectly with Git and the combination Git/DVC is one of the most popular choice for simple versioning.
- DVC works by supplementing each data file with a corresponding metadata file (.dvc), which is used to sync with a remote repository designed for large files (All the large files, datasets, models, etc. can be stored in remote storage servers (S3, Google Drive, etc).
- DVC supports easy-to-use commands to configure, push, pull datasets to remote storage.).
- Git tracks the metadata file, while DVC handles the remote repository.
***

## Installation
- Installation via pip with: `pip install dvc`
***

## DVC workflow
From a very high-level point of view, DVC works as follows:
  - Make sure you run the following command in the top level folder (where the hidden `.git` folder is). A Git project is initialised as a DVC project `dvc init` and a `.dvc` and `.dvcignore` folders are created to handle the configuration (similar to the `.git` folder). Inside it, a cache folder handles the local cache.
  - Adding a data file to the DVC version control system: `dvc add <file_path>` moves the file to the local cache, letting Git track only the corresponding `.dvc` file. Further, dvc add this file to `.gitignore` automatically so git will not upload the large file.
  - Add to git only the dvc file as: `git add <file_path.dvc>`. Please note the syntax `name.dvc`.
  - Files in the local cache can be synced with a remote repository `dvc push`.
  - At any time, files can be synced from the remote repository to the local cache `dvc fetch` or from the local cache to the working folder `dvc pull`.
***

## Configuring Google Drive as your remote storage
- You have two options to store your model:
    - Google Drive: free and the easiest to implement.
    - Use some cloud-based services such as S3 and although they are cheap you have to register.
- Create a folder in your Google Drive called `My_Folder_on_GoogleDrive`.
- Get the ID of this folder and the address will look like something like this: `https://drive.google.com/drive/u/0/folders/1A0zgCLZ1YF` where the ID the last alphanumeric block if this URL.

![image](https://user-images.githubusercontent.com/89139139/221132587-19c1d95e-45a0-45a0-993d-6bc25dcb2dd8.png)

- Add this storage: `dvc remote add -d storage gdrive://1A0zgCLZ1YF`
- Check the contents of the file `.dvc/config` whether the remote storage is configured correctly or not. Remember this is a hidden file, hence use: `ls -a` to see them.
***

## Pushing files
- Run the code with: `python train.py` which once finished should have saved the last checkpoint under the `./model/<checkpoint_name>.ckpt` folder.
- Add this file to the dvc registry with: `dvc add models/<checkpoint_name>.ckpt` pretty much as you would have done with a standard `git command`
- DVC creates 2 files when you run the `add` command: `.dvc` file and `.gitignore` file. So DVC takes care of not pushing the model to git because `git` is not really design for large file.
- Push push the model to the Google Drive: `dvc push trained_model.dvc` which will ask for some authentication.
- Now check if the model was updated to Google Drive.
- Add these two files: `git add models/trained_model.dvc ../models/.gitignore`
- Add a committment message `git commit -m "Added trained model to google drive using dvc"`
- Push `git push`
***

## Pulling files
- Pulling the file from dvc is as simple as: `dvc pull trained_model.dvc`
***

## References
- [Blog post](https://www.ravirajag.dev/blog/mlops-dvc)
- [GitHub code](https://github.com/graviraja/MLOps-Basics/tree/main/week_3_dvc)
- [Main GitHub project page](https://github.com/graviraja/MLOps-Basics)
- [DVC](https://dvc.org/)
- [DVC Documentation](https://dvc.org/doc)
- [DVC Tutorial on Versioning data](https://www.youtube.com/watch?v=kLKBcPonMYw)
***
