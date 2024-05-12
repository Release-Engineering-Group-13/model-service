# model-service


## How to run:
1. Pull and run the image (current image is not the final one)
     ```bash
    docker-compose up
    ```
2. Go to localhost:8080/apidocs
3. Click try it out button, then execute (currently returns errors due to non-functional predict method)

## TODOS:
- folder output content should be fetched frfom model-training somehow.
- docker-compose should not be in this repo but in operations. 
- Predicting with model does not work yet due to unrecognized data type.
- Workflow does not work due to uppercase characters in organization name (I can't change it).
- Unable to change image accessibility to public (I don't have access to organization settings). 
