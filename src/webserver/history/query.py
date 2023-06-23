import pandas as pd
import os
from datetime import datetime

class Query: 
    def __init__(self) -> None:
        self.file_path = './src/webserver/history/query_data.csv'
        if os.path.isfile(self.file_path):
            with open(self.file_path, 'rb') as file:
                self.query_data = pd.read_csv(file, index_col=0)
        else:
            self.query_data = pd.DataFrame(columns=['ID', 'Datum', 'Firmenname', 'Straße', 'Ort', 'Branche', 'Anzahl der Mitarbeiter', 'Telefon', 'E-Mail', 'Eingabeparameter', 'Ergebnisse der Abfrage', 'Feedback zur Abfrage', 'TCO', 'CLV', 'plot_data'])
            self.query_data.to_csv(self.file_path)

    def load_query_data(self):
        return self.query_data
    
    def save_query_data(self, data):
        self.query_data.loc[len(self.query_data)] = data
        self.query_data.to_csv(self.file_path)
        return