# Update the area of the bathroom to be 10.50 square meters instead of 9.50 using negative indexing.
# Make the areas list more trendy! Change "living room" to "chill zone". Don't use negative indexing this time.

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4] = "chill zone"

print(areas)