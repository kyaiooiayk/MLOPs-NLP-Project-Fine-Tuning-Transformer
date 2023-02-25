# Step 4 - Model serialisation - ONNX
- [ ] Step #0: Project Setup
- [ ] Step #1: Model monitoring - Weights and Biases
- [ ] Step #2: Configurations - Hydra
- [ ] Step #3: Data Version Control - DVC
- [x] Step #4: Model Serialisation - ONNX
- [ ] Step #5: Model Packaging - Docker
- [ ] Step #6: CI/CD - GitHub Actions
- [ ] Step #7: Container Registry - AWS ECR
- [ ] Step #8: Serverless Deployment - AWS Lambda
- [ ] Step #9: Prediction Monitoring - Kibana
***

## Virtual environment setup
- If you have your virtual environment created in week 0 active you are set to go, if not activate it with: `conda activate mlops`
- Install these additional packages:
    - `pip install onnx`
    - `pip install onnxruntime`
- After these extra packages were installed, save the new requirements file with: `pip freeze -> requirements.txt`
***

## Why ONNX?
- Why do we need model packaging? The best idea to understand this need is to think about deployment as someting different from training. Models can be built using any machine learning framework available out there (sklearn, tensorflow, pytorch, etc.). We might want to deploy models in different environments like (mobile, web, raspberry pi) or want to run in a different framework (trained in pytorch, inference in tensorflow).
- A common file format to enable AI developers to use models with a variety of frameworks, tools, runtimes, and compilers will help a lot.
- This is acheived by a community project `ONNX`.
***

## ONNX & ONNX Runtime
- **ONNX** introduces a new paradigm: converting it to a set of operations that can be executed directly by the framework. This allows to decouple the model from your current python and virtual environment packages. This allows the model to be portable to to many different languages. ONNX Runtime is a performance-focused inference engine for ONNX models. 
- *8ONNX Runtime** was designed with a focus on performance and scalability in order to support heavy workloads in high-scale production scenarios.
- Thus, ONNX is an open file format to store (**trained**) machine learning models/pipelines containing sufficient detail (regarding data types etc.) to move from one platform to another.
***

## Installation
- Install it with: `pip install onnxruntime`
- ONNX Runtime is supported on different Operating System (OS) and hardware (HW) platforms. The Execution Provider (EP) interface in ONNX Runtime enables easy integration with different HW accelerators. Check all the providers of ONNXRuntime using the command:
```python
from onnxruntime import  get_all_providers
print(get_all_providers())
```
***

## Exporting model to ONNX
- Since we are using Pytorch Lightning which is a wrapper around Vanilla Pytorch, there are two ways to convert the model intoocean format:
    - Using `onnx.export` method in PT, used in this tutorial.
    - Using `to_onnx` method in PT lightening
- Once the model is trained, convert the model using the following command: `python convert_model_to_onnx.py` which is going to write our converted model here: `./models/model.onnx`
***

## Inference
- Inference using standard pytorch: `python inference.py`
- Inference using ONNX Runtime: `python inference_onnx.py`
***

## References
- [Blog post](https://www.ravirajag.dev/blog/mlops-onnx)
- [GitHub code](https://github.com/graviraja/MLOps-Basics/tree/main/week_4_onnx)
- [Main GitHub project page](https://github.com/graviraja/MLOps-Basics)
- [ONNX](https://onnx.ai/)
- [ONNXRuntime](https://www.onnxruntime.ai/)
- [Abhishek Thakur tutorial on onnx model conversion](https://www.youtube.com/watch?v=7nutT3Aacyw)
- [Pytorch Lightning documentation on onnx conversion](https://pytorch-lightning.readthedocs.io/en/stable/common/production_inference.html)
- [Huggingface Blog on ONNXRuntime](https://medium.com/microsoftazure/accelerate-your-nlp-pipelines-using-hugging-face-transformers-and-onnx-runtime-2443578f4333)
- [Piotr Blog on onnx conversion](https://tugot17.github.io/data-science-blog/onnx/tutorial/2020/09/21/Exporting-lightning-model-to-onnx.html)
***