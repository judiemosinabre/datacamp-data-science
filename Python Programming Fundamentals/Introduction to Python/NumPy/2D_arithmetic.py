# np_baseball is coded for you; 
# it's again a 2D numpy array with 3 columns representing 
# height (in inches), 
# weight (in pounds) and age (in years). 

# baseball is available as a regular list of lists and updated is available as 2D numpy array.

# You managed to get hold of the changes in height, weight and age of all baseball players. It is available as a 2D numpy array, updated. Add np_baseball and updated and print out the result.
# You want to convert the units of height and weight to metric (meters and kilograms, respectively). As a first step, create a numpy array with three values: 0.0254, 0.453592 and 1. Name this array conversion.
# Multiply np_baseball with conversion and print out the result.

import numpy as np

np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
print(np_baseball + updated)

# Create numpy array: conversion
conversion = ([0.0254,0.453592,1])

# Print out product of np_baseball and conversion
print(np_baseball*conversion)