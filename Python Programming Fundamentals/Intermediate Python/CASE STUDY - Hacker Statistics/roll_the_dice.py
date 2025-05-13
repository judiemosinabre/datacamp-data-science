'''
As Hugo explained in the video you can just as well use randint(), 
also a function of the random package, to generate integers 
randomly. The following call generates the integer 1 to 6 randomly. 

7 is not included.
'''

# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Use randint() to simulate a dice
print(np.random.randint(1,7))

# Use randint() again
print(np.random.randint(1,7))