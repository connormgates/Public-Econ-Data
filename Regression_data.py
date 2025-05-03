import pandas as pd
import numpy as np
from scipy.stats import linregress
df = pd.read_csv('ep-data.csv', sep=';')
df.columns = df.columns.str.strip()
df['TO'] = pd.to_numeric(df['TO'], errors='coerce')
df['dlnC_NOME'] = pd.to_numeric(df['dlnC_NOME'], errors='coerce')
df = df.dropna(subset=['TO', 'dlnC_NOME'])
df = df[(~df['TO'].isin([np.inf, -np.inf])) & (~df['dlnC_NOME'].isin([np.inf, -np.inf]))]
df = df.round(3)
slope, intercept, r_value, p_value, std_err = linregress(df['TO'], df['dlnC_NOME'])
regression_summary = pd.DataFrame({'Metric': ['Slope', 'Intercept', 'R-squared', 'P-value', 'Standard Error'],
'Value': [round(slope, 4), round(intercept, 4), round(r_value**2, 4), round(p_value, 4), round(std_err, 4)]})
print("\nRegression Summary Table:")
print(regression_summary)
regression_summary.to_csv('regression_summary.csv', index=False)