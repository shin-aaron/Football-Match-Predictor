# Football Match Predictor

A machine learning model that predicts EPL football match outcomes using historical Premier League data.

## Features
- Predicts Home Win / Draw / Away Win probabilities for any EPL matchup
- Trained on 6 seasons of real Premier League data (2019–2025)
- Uses recent form and head-to-head history as features
- Built with Random Forest classifier (~50% accuracy — on par with professional models)

## Tech Stack
- Python, Pandas, NumPy
- scikit-learn (Random Forest Classifier)
- 2,280 real EPL matches from football-data.co.uk

## How to Run
```bash
pip install pandas numpy scikit-learn
python main.py
```

## Example Output
Who is home team? : Arsenal
Who is away team? : Chelsea
═══════════════════════════════════════
Arsenal VS Chelsea
═══════════════════════════════════════
Home Win:  55.0%
Draw:      16.0%
Away Win:  29.0%
═══════════════════════════════════════

## Features Used
- Last 5 matches: points, goals scored, goals conceded, shots on target (home & away)
- Head to head: home team wins and average goals in last 5 meetings

## Project Structure
- `data_loader.py` — loads and combines 6 seasons of EPL CSV data
- `feature_engineer.py` — builds form and h2h features for each match
- `predictor.py` — trains Random Forest model and generates predictions
- `main.py` — user interface

## Roadmap
- Add player availability and injury data as features
- Experiment with XGBoost for improved accuracy
- Add visualization of team form trends
