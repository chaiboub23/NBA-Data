import pandas as pd
import matplotlib.pyplot as plt
plt.close('all')
pd.set_option('display.max_columns', 500)
plt.gcf().subplots_adjust(bottom=0.15)
df = pd.read_csv('../all_seasons.csv')
# TODO: Find average and calculate who has an above average score.
