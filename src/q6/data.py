import pandas as pd
import matplotlib.pyplot as plt
plt.close('all')
data = {
    'Draft Status': ['Drafted', 'Undrafted'],
    'Points': [8.859373, 4.689893],
    'Rebounds': [3.843664, 2.230066], 
    'Assists': [1.921043, 1.240735]
}
df = pd.DataFrame(data, columns = ['Draft Status', 'Points', 'Rebounds', 'Assists'])
graph = df.plot.bar(color=['red', 'blue', 'green'], title="Drafted vs Undrafted Players Average Points, Rebounds, and Assists", x='Draft Status')
graph.set_xlabel("Draft Status")
graph.set_ylabel("Number of Points, Rebounds, or Assists")
plt.show()