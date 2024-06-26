"""
Flask API of the phishing link detection model.
"""

import os
import joblib
from flask import Flask, jsonify, request
from flasgger import Swagger

import numpy as np
from fetch_model import fetch_model

from lib_ml import preprocess_input
#from preprocessing import preprocess_input


app = Flask(__name__)
template = {
  "swagger": "2.0",
  "info": {
    "title": "Model Service API",
    "description": "API for the model service",
    "version": "1.0.0"
  },
  "basePath": os.environ.get("URL_PREFIX", ""),  
}
swagger = Swagger(app, template=template)


@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict whether a link is a phishing link.
    ---
    consumes:
      - application/json
    parameters:
        - name: input_data
          in: body
          description: link to be evaluated.
          required: True
          schema:
            type: object
            required: link
            properties:
                link:
                    type: string
                    example: https://www.tudelft.nl/en/student/administration/termination-of-enrolment
    responses:
      200:
        description: "The result of the classification: 'phishing' or 'legitimate'."
    """

    link = request.get_json().get('link')
    _, processed_link = preprocess_input(link)
    model = joblib.load('model/model.joblib')  # may have to change path in final version
    prediction = model.predict(processed_link)[0]
    prediction = (np.array(prediction) > 0.5).astype(int).tolist()  # 0 if phishing, 1 if legitimate
    print(link,prediction)

    res = {
        "Link": link,
        "Prediction": prediction
    }
    return jsonify(res)


if __name__ == '__main__':
    fetch_model()
    clf = joblib.load('model/model.joblib')
    app.run(host="0.0.0.0", port=8080, debug=True)
