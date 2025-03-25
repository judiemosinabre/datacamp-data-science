# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out observation for Japan
# print as a Series
print(cars.loc['JPN'])

# Print out observations for Australia and Egypt
# print as a DataFrame
print(cars.loc[['AUS','EG']])