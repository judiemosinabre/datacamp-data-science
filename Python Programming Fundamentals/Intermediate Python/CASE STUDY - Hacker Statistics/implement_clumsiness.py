'''
With this neatly written code of yours, 
changing the number of times the random walk should be simulated 
is super-easy. You simply update the range() 
function in the top-level for loop.

There's still something we forgot!
You're a bit clumsy and you have a 0.5% chance of falling down. 
That calls for another random number generation. 
Basically, you can generate a random float between 0 and 1. 
If this value is less than or equal to 0.005, 
you should reset step to 0.
'''

# numpy and matplotlib imported, seed set
import numpy as np
import matplotlib.pyplot as plt


# clear the plot so it doesn't get cluttered if you run this many times
plt.clf()

# Simulate random walk 20 times
all_walks = []
for i in range(20):
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        # Implement clumsiness
        if np.random.rand() <= 0.005 :
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show()