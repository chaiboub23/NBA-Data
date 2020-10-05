import pandas as pd
pd.set_option('display.max_columns', 500)
dfs = pd.read_csv('../all_seasons.csv')
short = dfs['player_height']<=200.8
# NOTE: This DataFrame contains the data for those below average height in the NBA.
dfs1 = dfs[short]
print(dfs1.head(10))