import pandas as pd
import matplotlib.pyplot as plt
plt.close('all')
df = pd.read_csv('../all_seasons.csv')
first_overall = df['draft_number']=='1'
df1 = df[first_overall]
df2 = df1[['college']]
df3 = df2['college'].value_counts()
df4 = df3.head(28)
df5 = df4.iloc[1:]
graph = df5.plot(
    kind='bar',
    x='college',
    y='count',
    title='Which College has the Most First Overall Picks',
    color='red'
)
graph.set_xlabel("College")
graph.set_ylabel("Number of Players")
plt.show()
