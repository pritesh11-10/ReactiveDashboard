import pandas as pd
import numpy as np


def load_dataset(path: str = "matches.csv"):
    matches = pd.read_csv(path, index_col=0)
    list_of_teams = np.unique(matches[["team1", "team2"]]).tolist()
    m_winner = matches[matches["toss_winner"] == matches["winner"]][['winner','season','date']]
    return matches, list_of_teams, m_winner


matches, list_of_teams, m_winner = load_dataset()