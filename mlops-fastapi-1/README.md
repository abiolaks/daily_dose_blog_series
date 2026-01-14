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
    * create dockerfile
    * ensure that docker is install on your system.
    * build the image using this comand - docker build -t iris-api .
    * run it using this - docker run -p 5000:80 iris-api

* Push the build image to your docker hub
    * Create a repo for this image in your docker hub
    * docker login in your development space( using terminal or docker destop) ( enter you docker id/username, password or PAT)
    * if using pAT ensure it has the permission to read, write and delete
    * Give you a local image a tag - docker tag iris-api abiolaks/mlops:v1.0  (docker tag name-of-image your-repo-address-hub:version_number)
    * Then push to your hub - docker push abiolaks/iris-api:v1.0
    * you should now see it in your docker hub. Anyone can download it as long as it is has public permission using docker pull abiolaks/mlops:v1.0 to thier machine.
    * Run it using docker run - docker run -p 5000:80 abiolaks/mlops:v1.0