# Week 4 - Model serialisation - ONNX
- [ ] Week 0: Project Setup
- [ ] Week 1: Model monitoring - Weights and Biases
- [ ] Week 2: Configurations - Hydra
- [ ] Week 3: Data Version Control - DVC
- [x] Week 4: Model Serialisation - ONNX
- [ ] Week 5: Model Packaging - Docker
- [ ] Week 6: CI/CD - GitHub Actions
- [ ] Week 7: Container Registry - AWS ECR
- [ ] Week 8: Serverless Deployment - AWS Lambda
- [ ] Week 9: Prediction Monitoring - Kibana
***


## Virtual environment setup
- If you have your virtual environment created in week 0 active you are set to go, if not activate it with: `conda activate mlops`
- Install these additional packages:
    - `pip install onnx`
    - `pip install onnxruntime`
- After these extra packages were installed, save the new requirements file with: `pip freeze -> requirements.txt`
***

## ONNX & ONNX Runtime
- ONNX introduces a new paradigm: converting it to a set of operations that can be executed directly by the framework. This allows to decouple the model from your current python and virtual environment packages. This allows the model to be portable to to many different languages. ONNX Runtime is a performance-focused inference engine for ONNX models. 
- ONNX Runtime was designed with a focus on performance and scalability in order to support heavy workloads in high-scale production scenarios.
***

## Exporting model to ONNX
- Once the model is trained, convert the model using the following command: `python convert_model_to_onnx.py`
***

## Inference
- Inference using standard pytorch: `python inference.py`
- Inference using ONNX Runtime: `python inference_onnx.py`
***

## References
- [Blog post](https://www.ravirajag.dev/blog/mlops-onnx)
- [GitHub code](https://github.com/graviraja/MLOps-Basics/tree/main/week_4_onnx)
- [Main GitHub project page](https://github.com/graviraja/MLOps-Basics)
***