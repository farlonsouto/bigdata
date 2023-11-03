import pandas as pd

dataFrame = pd.read_csv('H1.csv').dropna()
# print(dataFrame.columns.values)
# print(dataFrame.head(5))
valueCount = dataFrame['Country'].value_counts()
print(valueCount.head(10))

