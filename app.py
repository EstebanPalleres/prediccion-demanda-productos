from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Cargando el modelo y el escalador
model = joblib.load('random_forest_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    features = [data['features']]
    scaled_features = scaler.transform(features)
    prediction = model.predict(scaled_features)
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
