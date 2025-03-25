# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Extract drives_right column as Series: dr
dr = pd.Series(cars["drives_right"])

# Use dr to subset cars: sel
sel = cars[dr != False]

# Print sel
print(sel)

'''
output
         cars_per_cap        country  drives_right
    US            809  United States          True
    RU            200         Russia          True
    MOR            70        Morocco          True
    EG             45          Egypt          True

'''