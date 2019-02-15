import pandas as pd

pd.set_option('display.max_columns', 100)
excel_file='C:/Users/Yousuf Khan/Desktop/Assignment/California_fraud_data.xlsx'
data = pd.read_excel(excel_file,sheet_name='Sheet1')
print(data.describe())

import matplotlib.pyplot as plt
data.plot(kind='scatter', x='Amount', y='Fraud Class', color='red')
plt.show()

data['Device'].value_counts().plot('barh')
plt.show()

data['Fraud Class'].value_counts().plot('barh')
plt.show()

data['Type of credit card'].value_counts().plot('barh')
plt.show()

data['State'].value_counts().plot('barh')
plt.show()

data['Amount'].hist()
plt.show()

data.groupby(data["Date time"].dt.month).count().plot(kind="bar")
plt.show()

