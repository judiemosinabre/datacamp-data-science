'''
Things are shaping up nicely! We already have code that 
calculates our location in the Empire State Building after 100 dice throws. However, there's something we haven't thought 
about - we can't go below 0!

A typical way to solve problems like this is by using max(). 
If we pass max() two arguments, the biggest one gets returned. 
For example, to make sure that a variable x never goes below 10 
when we decrease it, you can use:
'''

# NumPy is imported, seed is set
import numpy as np

# Initialize random_walk
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        # Replace below: use max to make sure step can't go below 0
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

print(random_walk)