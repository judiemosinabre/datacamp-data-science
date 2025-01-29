# Delete the string and float for the "poolhouse" from your areas list.
# Print the updated areas list.

areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Delete the poolhouse items from the list
del areas[10:12]

# Print the updated list
print(areas)