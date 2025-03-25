# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Import numpy, you'll need this
import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]

# Print medium
print(cars)
print(medium)

'''
output:
         cars_per_cap        country  drives_right
    US            809  United States          True
    AUS           731      Australia         False
    JPN           588          Japan         False
    IN             18          India         False
    RU            200         Russia          True
    MOR            70        Morocco          True
    EG             45          Egypt          True
    
        cars_per_cap country  drives_right
    RU           200  Russia          True
'''