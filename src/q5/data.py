import pandas as pd
import matplotlib.pyplot as plt
plt.close('all')
data = {'Height': ['Tall', 'Short'],'Points': [7.730298668585823, 8.520619294791482], 'Assists': [1.1263404102195034, 2.473080365133345]}
df = pd.DataFrame(data, columns = ['Height', 'Points', 'Assists'])
graph = df.plot.bar(color=['red', 'blue'], title="Epic Graph\nAnother Line! Whoa", x='Height')
plt.show()