import pandas as pd
dfs = pd.read_csv('../all_seasons.csv')
short = dfs['player_height']<=200.8
dfs1 = dfs[short]
dfs2 = dfs1[['pts']]
dfs3 = dfs1[['ast']]
dfs4 = dfs2['pts'].mean()
dfs5 = dfs3['ast'].mean()