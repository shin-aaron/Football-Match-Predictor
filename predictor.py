from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
class Predictor:
    def __init__(self, features, fe):
        self.features = features
        self.fe = fe
    
    def train(self):
        self.features['result'] = self.features['result'].map({'H': 2, 'D': 1, 'A': 0})
        features = [
            'home_form_points', 'home_form_goals_scored', 'home_form_goals_conceded', 'home_form_shots_on_target',
            'away_form_points', 'away_form_goals_scored', 'away_form_goals_conceded', 'away_form_shots_on_target',
            'h2h_home_wins', 'h2h_avg_goals'
        ]
        X = self.features[features]
        y = self.features['result']
        X = X[(X['home_form_points'] != 0) | (X['away_form_points'] != 0)]
        y = y[X.index]  

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
        
        self.model = RandomForestClassifier()
        self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test)
        # for i in range(5):
        #     print(f"Predicted: {predictions[i]}  |  Actual: {y_test.iloc[i]}")
        
        accuracy = accuracy_score(y_test, predictions)
        print(f"Accuracy: {accuracy:.2%}")
    
    def predict_match(self, home_team, away_team):
        last_index = len(self.fe.data)
        home_matches = self.fe.get_team_form(home_team, last_index)
        home_stats = self.fe.calculate_form_stats(home_team, home_matches)
        away_matches = self.fe.get_team_form(away_team, last_index)
        away_stats = self.fe.calculate_form_stats(away_team, away_matches)
        h2h = self.fe.get_h2h_stats(home_team, away_team, last_index)

        row = {
                'home_form_points': home_stats['points'],
                'home_form_goals_scored': home_stats['goals_scored'],
                'home_form_goals_conceded': home_stats['goals_conceded'],
                'home_form_shots_on_target': home_stats['shots_on_target'],
                # add away stats and h2h stats...
                'away_form_points': away_stats['points'],
                'away_form_goals_scored': away_stats['goals_scored'],
                'away_form_goals_conceded': away_stats['goals_conceded'],
                'away_form_shots_on_target': away_stats['shots_on_target'],
                # h2h stats
                'h2h_home_wins': h2h['h2h_home_wins'],
                'h2h_avg_goals': h2h['h2h_avg_goals']
            }
        input_df = pd.DataFrame([row])
        probabilities = self.model.predict_proba(input_df)[0]
        return probabilities