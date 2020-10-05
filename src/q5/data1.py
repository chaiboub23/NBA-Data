import pandas as pd
pd.set_option('display.max_columns', 500)
dft = pd.read_csv('../all_seasons.csv')
tall = dft['player_height']>=200.8
# NOTE: This DataFrame contains the data for those above average height in the NBA.
dft1 = dft[tall]
dft2 = dft1[['pts']]
dft3 = dft1[['ast']]
dft4 = dft2['pts'].mean()
dft5 = dft3['ast'].mean()
print(dft4)
print(dft5)