from data_loader import DataLoader
from feature_engineer import FeatureEngineer
from predictor import Predictor

loader = DataLoader()
data = loader.load()
fe = FeatureEngineer(data)
features = fe.build_features()
predictor = Predictor(features, fe)

predictor.train()
home_team = input("Who is home team? : ")
away_team = input("Who is away team? : ")
predictor.predict_match(home_team, away_team)

probs = predictor.predict_match(home_team, away_team)

print(f"""
═══════════════════════════════════════
        {home_team} VS {away_team}
═══════════════════════════════════════
Home Win:  {probs[2]*100:.2f}%
Draw:      {probs[1]*100:.2f}%
Away Win:  {probs[0]*100:.2f}%
═══════════════════════════════════════
""")