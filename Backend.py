from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app)

# Load the entire stacking pipeline
stack_model = joblib.load("Finals_Model.pkl")

@app.route("/", methods=["GET"])
def home():
    return {"message": "Backend Running — Use /predict"}, 200


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # DataFrame with SAME column names as used in training
        df = pd.DataFrame([data])

        # Stacking model handles all preprocessing internally
        price = stack_model.predict(df)[0]

        return jsonify({"prediction": float(price)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
