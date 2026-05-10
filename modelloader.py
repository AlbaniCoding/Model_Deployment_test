import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "Models",
    "Naive Bayes for general.joblib"
)

model = joblib.load(MODEL_PATH)


def predict_news_type(text: str) -> str:
    return model.predict([text])[0]