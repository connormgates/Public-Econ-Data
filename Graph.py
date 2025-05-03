import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv('ep-data.csv', sep=';')
df.columns = df.columns.str.strip()
print(df.columns.tolist())
dr = df.dropna(subset=['dlnC_NOME','TO'])
plt.figure(figsize=(20, 10))
df = df.sort_values(by='TO')
plt.plot(df['TO'], df['dlnC_NOME'], marker='o', linestyle='-', color='blue')   
plt.title('Consumption Growth vs Trade Openness') 
plt.xlabel('Trade Openness (TO)')
plt.ylabel
plt.grid(True)
plt.savefig('graph_plot.png')
plt.show()
