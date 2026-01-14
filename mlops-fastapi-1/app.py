# Loads the model at startup and provides a prediction endpoint
from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel
from sklearn.datasets import load_iris

# define the input data model(4 features for iris dataset)
class IrisFeatures(BaseModel):
    """"Input data model validation for Iris features
        A pydanctic basemodel to validate the incoming Json request.
        Attributes:
            sepal_length (float): Sepal length of the iris flower.
            sepal_width (float): Sepal width of the iris flower.
            petal_length (float): Petal length of the iris flower.
            petal_width (float): Petal width of the iris flower.
    """
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Load the trained model at startup - this avoid reloading for each request
model = joblib.load("iris_model.pkl")
iris = load_iris() # Load iris dataset to get target names

# Initialize FastAPI app
app = FastAPI(title="Iris Species Prediction API") 


@app.get("/health") # To check if servie is alive
def health():
    return {"status": "alive"}

@app.post("/predict")
def predictS_species(features: IrisFeatures):
    # Convert input features to the format for model
    data = np.array([[features.sepal_length, features.sepal_width, features.petal_length, features.petal_width]])
    pred_class = model.predict(data)[0]
    # probabilities for each class
    pred_proba = model.predict_proba(data)[0]
    species_name = iris.target_names[pred_class]
    
    # probabilitie for each class
    confidence  = max(pred_proba)
    return {
        "predicted_species": species_name,
        "confidence": confidence
    }