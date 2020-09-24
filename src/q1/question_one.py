import pandas as pd
import matplotlib.pyplot as plt
plt.close('all')
plt.gcf().subplots_adjust(bottom=0.15)
df = pd.read_csv('../all_seasons.csv')
first_overall = df['draft_number']=='1'
df1 = df[first_overall]
df2 = df1.head(10)
df3 = df1[['college']]
df4 = df3['college'].value_counts()
df5 = df4.head(25)
df5.plot(kind='bar', x='college', y='count', title='test', color='red')
plt.show()
