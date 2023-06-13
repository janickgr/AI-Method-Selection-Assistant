import xgboost
import pickle
from utils import utils
import pandas as pd

# src/webserver/models/xgbc.pkl


class LGBModel: 

    def __init__(self) -> None:
        with open('src/webserver/models/lgbc.pkl', 'rb') as file:
            self.model = pickle.load(file)

    def get_predict_result_raw(self, input_data):
        prediction = self.model.predict_proba(input_data)
        return self.model.classes_[prediction.argsort()[0]]
    
    def get_predict_result_plot(self, input_data):
        names = utils.get_clean_methods_names(self.model.classes_)
        prediction = self.model.predict_proba(input_data)
        score = prediction[0]

        zipped_data = list(zip(names, score))

        df_zipped_data = pd.DataFrame(zipped_data, columns=['name', 'score'])
        df_sorted_by_score = df_zipped_data.sort_values(by='score', ascending=False)            

        return df_sorted_by_score
