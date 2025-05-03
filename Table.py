import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('ep-data.csv', sep=';')
df.columns = df.columns.str.strip()
print(df.columns.tolist())
df = df.dropna(subset=['dlnC_NOME', 'TO'])
df['TO'] = pd.to_numeric(df['TO'], errors='coerce')
df['dlnC_NOME'] = pd.to_numeric(df['dlnC_NOME'], errors='coerce')
df = df.dropna(subset=['TO', 'dlnC_NOME'])
df = df[(~df['TO'].isin([np.inf, -np.inf])) & (~df['dlnC_NOME'].isin([np.inf, -np.inf]))]
df = df.round(3)
df.to_csv('cleaned_table.csv', index=False)
plt.figure(figsize=(10, 6))

