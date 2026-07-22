import functions_framework
import joblib
import json

# 1. Load the "Brain" (The model you just trained)
# We load it at the top so it stays in memory (Fast!)
model = joblib.load('spam_classifier.joblib')

@functions_framework.http
def predict(request):
    # 2. Handle CORS (So your Frontend can talk to this Backend)
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)

    headers = {'Access-Control-Allow-Origin': '*'}

    # 3. Get the Email Text from the request
    request_json = request.get_json(silent=True)
    
    if request_json and 'message' in request_json:
        user_message = request_json['message']
        
        # 4. Make the Prediction
        prediction = model.predict([user_message])[0]
        
        # 5. Send back the result
        return (json.dumps({"prediction": prediction, "status": "success"}), 200, headers)
    
    return (json.dumps({"error": "No message provided"}), 400, headers)