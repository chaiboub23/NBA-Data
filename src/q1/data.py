# IMPORTS
import pandas as pd
import matplotlib.pyplot as plt
# Close all plots that may be open.
plt.close('all')
# Adjust the view of the plot to show more of the bottom of the plot
plt.gcf().subplots_adjust(bottom=0.15)
# Read the CSV file.
df = pd.read_csv('../all_seasons.csv')
# Filter to see where its a first overall pick or not.
first_overall = df['draft_number']=='1'
# Make a new dataframe that has only players that are first overall
df1 = df[first_overall]
# Make a dataframe that filters by college
df2 = df1[['college']]
# Dataframe that holds all the college values(total amount of colleges)
df3 = df2['college'].value_counts()
# Dataframe that holds the head of the data
df4 = df3.head(28)
df5 = df4.iloc[1:]
# Plot the graph
df5.plot(
    kind='bar',
    x='college',
    y='count',
    title='Which College has the Most First Overall Picks',
    color='red'
)
# Show the graph
plt.show()
