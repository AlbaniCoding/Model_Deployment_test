import joblib
def predict_news_type(text:str) -> str: 
    model = joblib.load('./Models/Naive Bayes for general.joblib')
    return model.predict([text])[0]


