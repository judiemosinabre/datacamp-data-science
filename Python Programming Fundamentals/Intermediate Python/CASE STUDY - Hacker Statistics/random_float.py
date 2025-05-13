''' All the functionality you need is contained in 
the random package, a sub-package of numpy. 
In this exercise, you'll be using two functions 
from this package:

seed(): sets the random seed, so that your results are reproducible between simulations. 
As an argument, it takes an integer of your choosing. If you call the function, 
no output will be generated.

rand(): if you don't specify any arguments, 
it generates a random float between zero and one. '''

# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)

# Generate and print random float
print(np.random.rand())