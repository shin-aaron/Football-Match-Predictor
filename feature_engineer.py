import pandas as pd
class FeatureEngineer:
    def __init__(self, data):
        self.data = data
    
    def get_team_form(self, team, before_index):
        filtered = self.data.iloc[:before_index]
        filtered_team = filtered[
        (filtered['HomeTeam'] == team) | 
        (filtered['AwayTeam'] == team) 
        ]
        lastfive = filtered_team.tail(5)
        return lastfive
    
    def calculate_form_stats(self, team, matches):
        points = 0
        goals_scored = 0
        goals_conceded=0
        shots_on_target=0
        for idx, row in matches.iterrows():
            if row['HomeTeam'] == team:
                goals_scored += row['FTHG']
                goals_conceded += row['FTAG']
                shots_on_target += row['HST']
                if row['FTR'] == "H":
                    points+=3
                elif row['FTR'] == "D":
                    points+=1
                
            else:
                goals_scored += row['FTAG']
                goals_conceded += row['FTHG']
                shots_on_target += row['AST']
                if row['FTR'] == "D":
                    points+=1
                elif row['FTR'] == "A":
                    points+=3
        
        return {
            'points': points,
            'goals_scored': goals_scored,
            'goals_conceded': goals_conceded,
            'shots_on_target': shots_on_target
        }
    
    def get_h2h_stats(self, home_team, away_team, before_index):
        after_filter = self.data.iloc[:before_index]
        after_filtered = after_filter[((after_filter['HomeTeam'] == home_team) & (after_filter['AwayTeam'] == away_team)) | ((after_filter['HomeTeam'] == away_team) & (after_filter['AwayTeam'] == home_team))]
        recent_five = after_filtered.tail(5)
        h2h_home_wins = 0
        h2h_avg_goals = 0.0
        for f, row in recent_five.iterrows():
            if row['HomeTeam'] == home_team and row['FTR'] == "H":
                h2h_home_wins += 1
                
            elif row['AwayTeam'] == home_team and row['FTR'] == "A":
                h2h_home_wins += 1
                
        if len(recent_five) > 0:
            h2h_avg_goals = (recent_five['FTHG'] + recent_five['FTAG']).mean()
        else:
            h2h_avg_goals = 0.0
        
        return {
            'h2h_home_wins': h2h_home_wins,
            'h2h_avg_goals': h2h_avg_goals
        }
    
    def build_features(self):
        rows = []
        for i, match in self.data.iterrows():
            home_team = match['HomeTeam']
            away_team = match['AwayTeam']

            # get form for both teams
            home_matches = self.get_team_form(home_team, i)
            home_stats = self.calculate_form_stats(home_team, home_matches)

            # do the same for away team
            away_matches = self.get_team_form(away_team, i)
            away_stats = self.calculate_form_stats(away_team, away_matches)

            # get h2h stats
            h2h = self.get_h2h_stats(home_team, away_team, i)

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
                'h2h_avg_goals': h2h['h2h_avg_goals'],
                'result': match['FTR']
            }
            rows.append(row)

        return pd.DataFrame(rows)