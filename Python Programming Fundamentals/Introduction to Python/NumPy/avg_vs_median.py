import numpy as np

# Create np_height_in from np_baseball
# Create numpy array np_height_in that is equal to first column of np_baseball.
np_height_in = np.array(np_baseball[:,0])

# Print out the mean of np_height_in
print(np.mean(np_height_in))


# Print out the median of np_height_in
print(np.median(np_height_in))
