import numpy as np

# np.random.normal here:
# distribution mean
# distribution standard deviation
# number of samples

height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
weight = np.round(np.random.normal(60.32, 15, 5000), 2)

np_city = np.column_stack((height, weight))
print(np_city)
print(np_city.shape)