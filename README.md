# model-service


## How to run:
1. cd to directory where docker-compose.yml resides
2. Pull and run the image 
     ```bash
    docker-compose up
    ```
3. Go to localhost:8080/apidocs
4. Click try it out button, then execute 

## TODOS:
- folder output content should be fetched from model-training somehow.
- docker-compose should not be in this repo but in operations. 
- Workflow does not work due to uppercase characters in organization name (I can't change the name).
- Unable to change image accessibility to public (I don't have access to organization settings). Remove test versions in organization registry before making public (I can't do this either). 
