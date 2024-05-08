"""
Flask API of the SMS Spam detection model model.
"""
#import traceback
import joblib
from flask import Flask, jsonify, request
from flasgger import Swagger
#import pandas as pd
import numpy as np

#from text_preprocessing import prepare, _extract_message_len, _text_process
from preprocessing import tokenize_single # Should eventually be from lib-ml

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/', methods=['POST'])
def predict(): # Change this specification
    """
    Predict whether an SMS is Spam.
    ---
    consumes:
      - application/json
    parameters:
        - name: input_data
          in: body
          description: message to be classified.
          required: True
          schema:
            type: object
            required: sms
            properties:
                sms:
                    type: string
                    example: This is an example of an SMS.
    responses:
      200:
        description: "The result of the classification: 'spam' or 'ham'."
    """
    #input_data = request.get_json()
    link = request.get_json().get('link')
    processed_link = tokenize_single(link)
    print("Processed link: ", processed_link)
    model = joblib.load('output/model.joblib') # Should eventually be downloaded from remote
    #prediction = model.predict(processed_link)[0]
    prediction = model.predict(processed_link)
    print("Length of prediction: ", len(prediction))
    prediction = (np.array(prediction) > 0.5).astype(int)
    print("Length of link: ", len(link))
    
    #res = {
    #    "result": "prediction",
    #    "classifier": "decision tree",
    #    "link": link
    #}
    #print(res)
    #return jsonify(res)
    res = {
        "Prediction" : prediction.tolist(),
        "Link" : link
    }
    return jsonify(res)

if __name__ == '__main__':
    clf = joblib.load('output/model.joblib')
    app.run(host="0.0.0.0", port=8080, debug=True)