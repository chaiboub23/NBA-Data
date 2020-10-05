import pandas as pd
pd.set_option('display.max_columns', 500)
dft = pd.read_csv('../all_seasons.csv')
tall = dft['player_height']>=200.8
# NOTE: This DataFrame contains the data for those above average height in the NBA.
dft1 = dft[tall]