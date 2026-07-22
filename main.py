import functions_framework
import joblib
import json

model = joblib.load('spam_classifier.joblib')

@functions_framework.http
def predict(request):
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)

    headers = {'Access-Control-Allow-Origin': '*'}

    request_json = request.get_json(silent=True)
    
    if request_json and 'message' in request_json:
        user_message = request_json['message']

        prediction = model.predict([user_message])[0]
        
        return (json.dumps({"prediction": prediction, "status": "success"}), 200, headers)
    
    return (json.dumps({"error": "No message provided"}), 400, headers)