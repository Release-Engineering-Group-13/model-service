# model-service


## How to run:
1. cd to directory where docker-compose.yml resides
2. Pull and run the image (current image is not the final one)
     ```bash
    docker-compose up
    ```
3. Go to localhost:8080/apidocs
4. Click try it out button, then execute (currently returns errors due to non-functional predict method)

## TODOS:
- folder output content should be fetched from model-training somehow.
- docker-compose should not be in this repo but in operations. 
- Predicting with model does not work yet due to unrecognized data type (should work after approving pr on lib-ml).
- Workflow does not work due to uppercase characters in organization name (I can't change the name).
- Unable to change image accessibility to public (I don't have access to organization settings). Remove test versions in organization registry before making public (I can't do this either). 
