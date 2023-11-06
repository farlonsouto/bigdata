import pandas as pd
import matplotlib.pyplot as plt
import calendar

dataFrame = pd.read_csv('H1.csv').dropna()
# print(dataFrame.columns.values)
# print(dataFrame.head(5))

# Task 1: The top 10 countries from which the most customers come.
valueCount = dataFrame['Country'].value_counts()
print("Task 1 - Top 10 countries costumers come from: \n {} \n".format(valueCount.head(10)))

# Task 2: Remove all cancelled orders + an overview of how much was has earned from each segment.
mask = dataFrame['IsCanceled'] == 1
noCancellationsDf = dataFrame[~mask]
earnedPerSegment = noCancellationsDf.groupby('MarketSegment')['ADR'].sum()
print('Task 2 - Earning amount per market segment: \n {} \n'.format(earnedPerSegment))

# Task 3: A simple histogram showing the rooms' prices (ADR)
print("Task 3 - Roms\' price histogram \n")
dataFrame.hist(column='ADR', bins=5, grid=False, figsize=(12, 8), color='#93184A', zorder=2, rwidth=0.9)
plt.show()

# Task 4:
# (Data analysis/visualization) For each month of the year 2016, create a line diagram with two
# graphs (in the same the diagram). The first graph should be the average of the price for all the
# rooms for that month, while the second graph should be the number of cancellations for that month.
# Include a legend that shows which graph is what. The months should lie on the x-axis

monthsNames = list(calendar.month_name)
""" 
month_to_num_dict = {}
num_to_month_dict = {}
for month in monthsNames:
    month_to_num_dict.update({month: monthsNames.index(month)})
    num_to_month_dict.update({monthsNames.index(month): month})
dataFrame['ArrivalDateMonth'] = dataFrame['ArrivalDateMonth'].map(month_to_num_dict)
"""

df_2016 = dataFrame.loc[dataFrame["ArrivalDateYear"] == 2016]
averageRoomPriceMonthly = df_2016.groupby('ArrivalDateMonth')['ADR'].mean()
averageRoomPriceMonthly.reindex(monthsNames)
averageRoomPriceMonthly.plot()
cancellationsMonthly = df_2016.groupby('ArrivalDateMonth')['IsCanceled'].sum()
cancellationsMonthly.reindex(monthsNames)
cancellationsMonthly.plot()
plt.show()
