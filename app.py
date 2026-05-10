from flask import Flask, request, jsonify, render_template
from modelloader import predict_news_type

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        text = data.get("text", "")

        prediction = predict_news_type(text)

        return jsonify({
            "prediction": prediction
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


# IMPORTANT FOR VERCEL
app = app