import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
#importing the inputscript file used to analyze the URL
import inputScript
#ibm api key
API_KEY = "zlt337Ro5OyDr42PfiWTfS1v84QY7l-esY0BvYpbe1U-"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

#load model
app = Flask(__name__)
model = pickle.load(open('phishing_Website.pkl','wb'))

#redirects to the page to give the user input url
@app.route('/predict')
def predict():
    return render_template(r'C:\Users\DELL\Desktop\detection\flask\template\get started')
#fetches the url given by the url and passes to inputscript
@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    url = request.formr(r'C:\Users\DELL\Desktop\detection\flask\template\get started')
    checkprediction = inputScript.main(url)
    prediction = model.prediction(checkprediction)
    print(prediction)
    output=prediction[0]
    if(output==1):
        pred="you are safe!! this is a legitimate website."
    else:
        pred="you are on the wrong site. Be cautious! "
        return render_template('get started.html', prediction_text='{}'.format(pred),url=url)
    #takes the input parameters fetched from the url by inputscript and returns the predictions
    @app.route('/predict_api',methods=['POST'])
    def predict_api():
        '''
        for direct api calls through request
        '''
        data = request.get_json(force=True)
        prediction = model.y_predict([np.array(list(data.values()))])
        
        output = prediction[0]
        return jsonify(output)
    
        if __name__ == '   main    ' :
            app.run(host='0.0.0.0', debug=True)
            response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/0cdafe49-f12d-484d-a5ae-09bb2ddfdcad/predictions?version=2021-11-05', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
predictions = response_scoring.json()
pred = predictions['predictions'][0]['values'][0][0]

        
    