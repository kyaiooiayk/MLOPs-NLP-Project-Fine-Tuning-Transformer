# Steep 7 - Container Registry - AWS ECR
- [ ] Step #0: Project Setup
- [ ] Step #1: Model monitoring - Weights and Biases
- [ ] Step #2: Configurations - Hydra
- [ ] Step #3: Data Version Control - DVC
- [ ] Step #4: Model Serialisation - ONNX
- [ ] Step #5: Model Packaging - Docker
- [ ] Step #6: CI/CD - GitHub Actions
- [x] Step #7: Container Registry - AWS ECR
- [ ] Step #8: Serverless Deployment - AWS Lambda
- [ ] Step #9: Prediction Monitoring - Kibana
***

## Virtual environment setup
- If you have your virtual environment created in step #0 active you are set to go, if not activate it with: `conda activate mlops`
- Install these additional packages: 
    - `pip install boto3`
    - `pip install "dvc[s3]"`
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

## AWS intro
- In brief (really compressing a lot here), AWS is cloud computing service based on  a client-server model. In computing, a client can be a web browser or desktop application that a person interacts with to make requests to computer servers. A server can be services such as Amazon Elastic Compute Cloud (Amazon EC2), a type of virtual server. Cloud computing is the on-demand delivery of IT resources over the Internet with pay-as-you-go pricing.
- You will have to create an account on AWS to able to follow this tutorial.
- More information/tutorials on AWS can be found [here](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/AWS).
***

## AWS S3 bucket
- Amazon Simple Storage Service (S3) is a storage object in the cloud.
- It is designed for large-capacity, low-cost storage provision across multiple geographical regions. 
- Amazon S3 provides developers and IT teams with Secure, Durable and Highly Scalable object storage.
- You can interact with AWS S3 bucket in many differet [ways](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/AWS#ways-to-interact-with-aws-services).
- Further notes on how to use `boto3` are availbale [here](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/AWS/AWS_S3)
***

## Creating a S3 bucket via AWS Management Console
- Sign in to the AWS Management Console: https://console.aws.amazon.com
- Navigate to open the Amazon S3 console at https://console.aws.amazon.com/s3/
- Click on `Create Bucket` and fill in the requested inputs
- Upload via the GUI any sample file you may wish to bring onto the S3.
***

## Accessing S3 via CLI
- We first need to get the credentials.
- Navigate to `My Security Credentials`
- Navigate to `Access Keys` section and click on `Create New Access Key` button. This will download locally a file containing both your `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` which are supposed to remain secret!
- export both of them in your environment variables so you do not have to copy-and-paste them all the time:
```shell
export AWS_ACCESS_KEY_ID=<ACCESS KEY ID>
export AWS_SECRET_ACCESS_KEY=<ACCESS SECRET>
```
***

## Accessing S3 using CLI
- Install the AWS CLI interface following [these instructions](https://aws.amazon.com/cli/)
- Check the s3 bucket content: `aws s3 ls s3://<your_s3_bucket_name>`
***

## Accessing S3 via boto3
- Access and print the content of yours s3 bucket
```python
import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('<your_s3_bucket_name>')
for obj in bucket.objects.all():
    print(obj.key)
```
***

## Configuring AWS S3 as remote storage in DVC
- In the previous tutorials we have seen how we could load our trained model on Google Drive and retrieve the same programmaticly. Here we'll try to do the same but instead of Google Drive, we'll use AWS S3. 
- Let's create a folder called `<your_s3_bucket_name>/trained_models` which will be used for storing the trained models.
- Initialise DVC (if not initialised) using the following command: `dvc init`
- Navigate to the new folder on the `AWS Management Console` and click on `Copy S3 URI` to copy the identifier.
- Add the s3 folder as remote storage for models in dvc: `dvc remote add -d model-store s3://<>your_s3_backet_name/trained_models/`
- Navigate to: `cd dvcfiles`
- Add the trained model to DVC: `dvc add ../models/model.onnx --file trained_model.dvc`
- Push the model to remote storage: `dvc push trained_model.dvc`
- Upon refreshing the S3 bucket you should be able to see your model uploaded in the S3 bucket storage object.
***

## ECR vs. S3
- ECR basically operates as a proxy in front of S3 to facilitate container build-operations. Same as DockerHub or Docker Registry, this can reduce the amount of stored data by storing each layer of a container image and not duplicating the same layer over and over again (saves you storage space).
- **If you were to just store a container image** in a S3 bucket you'll not do it effienctly as the amount of storage we'd likekly double due to the lack of layer de-duplication that would be occurring when using ECR. 
- **Example**: you build version 1 of a container image for your app, total size is 50MB. Then you make an update to you image that only affects the last RUN statement in your Dockerfile (only one layer of the image is changed)... that one layer is 2MB, so when you push that new version ECR will upload the 2MB layer, not the other 48MB that hasn't changed. This would amount to 100MB of storage in S3.
- If you want to read more about Docker, Container see [this](https://github.com/kyaiooiayk/Docker-Notes).
***

## ECR
- In step #6 we have build container using CICD. This allows us to check everything went through OK on both integration and deployment tests. However, the image is not persisted anywhere for further usage. This is where Container Registry comes into the picture.
- A container registry is a place to store container images. Hosting all the images in one stored location allows users to commit, identify and pull images when needed. 
***

## Setting up AWS ECR
- Navigate to your `AWS Management Console` Search for ECR and click on `Get Started`.
- Create a repository when prompted and give it a name name.
- Update the `Dockerfile` to accomodate the changes from Google Drive to AWS S3.
- Build the Docker image using the command: `docker build --build-arg AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID --build-arg AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY  -t inference:test .`
-Navigate to the `ECR Navigation Console` and click on `View push command`. It looks like something like this: `aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 246113150184.dkr.ecr.us-west-2.amazonaws.com`
- Tagging the image: `Docker tag inference:test 246113150184.dkr.ecr.us-west-2.amazonaws.com/mlops-basics:latest`
- Pushing the image: `docker push 246113150184.dkr.ecr.us-west-2.amazonaws.com/mlops-basics:latest`
***

## Configuring GitHub Actions to use S3, ECR
- At this points we have a `latest_model.checkpoint` and an image stored in S3 and ECR respectively. Thus, out next step will be how to make sure that when an action is trigger via GitHub Actinons this is able to push/pull to both S3 and ECR.
- Navigate to your GitHub repositor and click on the `Settings` tab
- Navigate to the `Secrets` section and click on `New repository secret`
- Save the following secrets: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` and `AWS_ACCOUNT_ID`
- These values can be used in GitHub Actions in the following manner: `AWS_ACCESS_KEY_ID: {{secrets.AWS_ACCESS_KEY_ID}}`
- Now we can modify the GitHub Action workflow again. [GitHub Actions Marketplace](https://github.com/marketplace?type=actions) comes with lot of predefined actions which are useful for us. Two in partiular are:
    - `aws-actions/configure-aws-credentials@v1` will be useful to configure AWS credential environment variables for use in other GitHub Actions.
    - `jwalton/gh-ecr-push@v1` will be useful to push/pull the image to ECR.
- Create a hidden folder and a file called `wokflows` using the command: `mkdir .github/workflows` with the followin content. If the file is already there then: `vim .github/workflows`. This file has the following content:
```shell
name: Create Docker Container

on: [push]

jobs:
  mlops-container:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: ./step_7_ecr
    steps:
      - name: Checkout
        uses: actions/checkout@v2
        with:
          ref: ${{ github.ref }}
      - name: Configure AWS Credentials
        uses: aws-actions/configure-aws-credentials@v1
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-west-2
      - name: Build container
        run: |
          docker build --build-arg AWS_ACCOUNT_ID=${{ secrets.AWS_ACCOUNT_ID }} \
                       --build-arg AWS_ACCESS_KEY_ID=${{ secrets.AWS_ACCESS_KEY_ID }} \
                       --build-arg AWS_SECRET_ACCESS_KEY=${{ secrets.AWS_SECRET_ACCESS_KEY }} \
                       --tag mlops-basics .
      - name: Push2ECR
        id: ecr
        uses: jwalton/gh-ecr-push@v1
        with:
          access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          region: us-west-2
          image: mlops-basics:latest
```
***

## References
- [Blog post](https://www.ravirajag.dev/blog/mlops-container-registry)
- [GitHub code](https://github.com/graviraja/MLOps-Basics/tree/main/week_7_ecr)
- [Main GitHub project page](https://github.com/graviraja/MLOps-Basics)
- [An introduction to what AWS is](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/AWS)
***