# Minimalistic view of MOdel deployment to Production
## Steps 
* Train the model and serialize the model in the train.py
* create the fastapi api endpoint for the model in app.py file
* enter the dependencies in the requirements.txt file
* Start the server using.
```
    uvicorn app:app --reload --port 5000
```
* test the api endpoint
* package the application using containers
