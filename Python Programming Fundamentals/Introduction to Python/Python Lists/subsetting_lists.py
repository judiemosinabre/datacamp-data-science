# To subset lists of lists, you can use the same technique as before: square brackets. 
# This would look something like this for a list, house:

# house[2][0]

# Subset the house list to get the float 9.5.
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Subset the house list
house[-1][1]