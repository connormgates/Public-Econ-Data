import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt 
import seaborn as sns
df = pd.read_csv('ep-data.csv', sep=';')
df.columns = df.columns.str.strip()
print(df.columns.tolist())
df = df.dropna(subset=['dlnC_NOME','TO'])
X = df[['TO']]
y = df['dlnC_NOME']
model = LinearRegression()
model.fit(X, y)
df['predicted'] = model.predict(X)
sns.scatterplot(x='TO', y='dlnC_NOME', data=df)
plt.plot(df['TO'], df['predicted'], color='red')
plt.xlabel('Trade Openness (TO)')
plt.ylabel('Consumption Growth vs Trade Openness')
plt.savefig('regression_plot.png')

