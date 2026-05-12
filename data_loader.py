import pandas as pd

class DataLoader:
    def __init__(self):
        self.files = [
            'pl_1920.csv', 'pl_2021.csv', 'pl_2122.csv',
            'pl_2223.csv', 'pl_2324.csv', 'pl_2425.csv'
        ]
        self.columns = [
            'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR',
            'HS', 'AS', 'HST', 'AST', 'HF', 'AF',
            'HC', 'AC', 'HY', 'AY', 'HR', 'AR'
        ]
        self.data = None
    def load(self):
        df_list = [pd.read_csv(f, usecols=self.columns) for f in self.files]
        self.data = pd.concat(df_list, ignore_index=True)
        return self.data