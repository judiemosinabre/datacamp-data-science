# Use the + operator to paste the list ["poolhouse", 24.5] to the end of the areas list. Store the resulting list as areas_1.
# Further extend areas_1 by adding data on your garage. Add the string "garage" and float 15.45. Name the resulting list areas_2.

# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 +["garage", 15.45]

print(areas_1)
print(areas_2)