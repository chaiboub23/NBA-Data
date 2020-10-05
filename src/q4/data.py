import pandas as pd
import matplotlib.pyplot as plt
plt.close('all')
pd.set_option('display.max_columns', 500)
plt.gcf().subplots_adjust(bottom=0.15)
df = pd.read_csv('../all_seasons.csv')
# NOTE: Average height is 6'7", or 79", or 200.8 cm.
above = df['player_height']>=200.8
df1 = df[above]
df2 = df1[['team_abbreviation']]
df3 = df2['team_abbreviation'].value_counts()
df4 = df3.head(30)
graph = df4.plot(
    kind='bar',
    x='team_abbreviation',
    y='count',
    title='Which Team has Players Taller than 200.8 cm',
    color='red'
)
graph.set_xlabel("Team (Abbreviation)")
graph.set_ylabel("Number of Players")
plt.show()