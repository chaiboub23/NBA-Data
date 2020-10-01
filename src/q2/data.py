import pandas as pd
import matplotlib.pyplot as plt
plt.close('all')
plt.gcf().subplots_adjust(bottom=0.15)
df = pd.read_csv('../all_seasons.csv')
df1 = df[['college']]
df2 = df1['college'].value_counts()
df3 = df2.head(26)
df4 = df3.iloc[1:]
df3.plot(kind='bar', x='college', y='count', title='Which College has the Most Drafted Players', color='red')
plt.show()
