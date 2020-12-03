import os
import pickle
import json
import numpy
import joblib
from sklearn.linear_model import Ridge


def init():
    global model
    # AZUREML_MODEL_DIR is an environment variable created during deployment.
    # It is the path to the model folder (./azureml-models/$MODEL_NAME/$VERSION)
    # For multiple models, it points to the folder containing all deployed models (./azureml-models)
    ##model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'sklearn_regression_model.pkl')
    # deserialize the model file back into a sklearn model
    ##model = joblib.load(model_path)

    # Update to your model's filename
    model_filename = "ridge_0.40.pkl"

    # AZUREML_MODEL_DIR is injected by AML
    model_dir = os.getenv('AZUREML_MODEL_DIR')

    print("Model dir:", model_dir)
    print("Model filename:", model_filename)
    
    model_path = os.path.join(model_dir, model_filename)

    # Replace this line with your model loading code
    model = joblib.load(model_path)

# note you can pass in multiple rows for scoring
def run(raw_data):
    try:
        data = json.loads(raw_data)['data']
        data = numpy.array(data)
        result = model.predict(data)
        # you can return any data type as long as it is JSON-serializable
        return result.tolist()
    except Exception as e:
        error = str(e)
        return error
