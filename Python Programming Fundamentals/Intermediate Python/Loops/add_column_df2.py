''' Using iterrows() to iterate over every observation of a 
Pandas DataFrame is easy to understand, but not very efficient. 
On every iteration, you're creating a new Pandas Series.

If you want to add a column to a DataFrame by 
calling a function on another column, 
the iterrows() method in combination with a for loop is 
not the preferred way to go. 

Instead, you'll want to use apply().'''


# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)

print(cars)