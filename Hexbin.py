import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('ep-data.csv', sep=';')
df.columns = df.columns.str.strip()
print(df.columns.tolist())
df = df.dropna(subset=['dlnC_NOME', 'TO'])
df = df[(~df['TO'].isin([np.inf, -np.inf])) & (~df['dlnC_NOME'].isin([np.inf, -np.inf]))]
df['TO'] = pd.to_numeric(df['TO'], errors='coerce')
df['dlnC_NOME'] = pd.to_numeric(df['dlnC_NOME'], errors='coerce')
plt.figure(figsize=(16,8))
plt.hexbin(df['TO'], df['dlnC_NOME'], gridsize=50, cmap='Blues')
plt.colorbar(label='Count')
z = np.polyfit(df['TO'], df['dlnC_NOME'], 1)
p = np.poly1d(z)
plt.plot(df['TO'], p(df['TO']), "r--", linewidth=2)
plt.xlim(0, 1.2)
plt.ylim(-20, 20)
plt.title('Consumption Growth vs Trade Openness (Hexbin)')
plt.xlabel('Trade Openness (TO)')
plt.ylabel('Consumption Growth (dlnC_NOME)')
plt.savefig('hexbin_plot.png')
plt.grid(True)
plt.show()