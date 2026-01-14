import requests
import time

data = {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}

start = time.time()
response = requests.post("http://localhost:5000/predict", json=data)
end = time.time()
print(f"Prediction took {end - start} seconds")