# Change the second command, that creates the variable areas_copy, 
# such that areas_copy is an explicit copy of areas. After your edit, 
# changes made to areas_copy shouldn't affect areas. Submit the answer to check this.


# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change this command
areas_copy = areas[:]

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)