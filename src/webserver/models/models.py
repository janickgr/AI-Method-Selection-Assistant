import xgboost
import pickle

# src/webserver/models/xgbc.pkl


def load_model_xgb():
    with open('src/webserver/models/xgbc.pkl', 'rb') as file:
        return pickle.load(file)


def xgb_predict(input_data, xgb_model):
    xgb_model_prediction = xgb_model.predict_proba(input_data)
    return xgb_model.classes_[xgb_model_prediction.argsort()]
