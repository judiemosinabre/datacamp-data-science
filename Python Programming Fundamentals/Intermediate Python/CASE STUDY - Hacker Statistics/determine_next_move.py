'''
In the Empire State Building bet, 
your next move depends on the number you get after throwing the dice. 
'''

import numpy as np
# NumPy is imported, seed is set
# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)

# Finish the control construct
if dice <= 2 : #If dice is 1 or 2
    step = step - 1
elif dice <= 5 : #If dice is 3, 4, or 5
   step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice, step)