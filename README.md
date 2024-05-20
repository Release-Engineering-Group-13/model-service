# model-service


## How to run model-service in isolation:
0. If the trained model has not been downloaded yet, install ellipsis and fetch the model. Otherwise, ignore this step
    ```bash
    pip install ellipsis
    python fetch_model.py
    ```
1. cd to directory where docker-compose.yml resides
2. Pull and run the image 
     ```bash
    docker-compose up
    ```
3. Go to localhost:8080/apidocs
4. Click try it out button, then execute 

## TODOS:
- docker-compose should not be in this repo but in operations along with corresponding instructions. 
