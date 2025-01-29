# Use slicing to create a list, downstairs, that contains the first 6 elements of areas.
# Create upstairs, as the last 4 elements of areas. This time, simplify the slicing by omitting the end index.
# Print both downstairs and upstairs using print().

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[:6]

# Use slicing to create upstairs
upstairs = areas[6:]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)