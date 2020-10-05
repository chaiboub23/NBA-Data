import pandas as pd
df = pd.read_csv('../all_seasons.csv')
drafted = df['draft_number']!='Undrafted'
undrafted = df['draft_number']=='Undrafted'
df1 = df[drafted]
df2 = df1[['pts']]
df_pts = df2.mean()
df3 = df1[['reb']]
df_reb = df3.mean()
df4 = df1[['ast']]
df_ast = df4.mean()
df5 = df[undrafted]
df6 = df5[['pts']]
df1_pts = df6.mean()
df7 = df5[['reb']]
df1_reb = df7.mean()
df8 = df5[['ast']]
df1_ast = df8.mean()