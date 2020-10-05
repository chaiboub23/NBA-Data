import pandas as pd
dft = pd.read_csv('../all_seasons.csv')
tall = dft['player_height']>=200.8
dft1 = dft[tall]
dft2 = dft1[['pts']]
dft3 = dft1[['ast']]
dft4 = dft2['pts'].mean()
dft5 = dft3['ast'].mean()