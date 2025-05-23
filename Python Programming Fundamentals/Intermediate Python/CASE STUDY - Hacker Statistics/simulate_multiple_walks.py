'''
A single random walk is one thing, 
but that doesn't tell you if you have a good chance at winning the bet.

To get an idea about how big your chances are of reaching 60 steps, 
you can repeatedly simulate the random walk and collect the results. T
hat's exactly what you'll do in this exercise.

The sample code already sets you off in the right direction. 
Another for loop is wrapped around the code you already wrote. 
It's up to you to add some bits and pieces to 
make sure all of the results are recorded correctly.
'''
# NumPy is imported; seed is set

# Initialize all_walks (don't change this line)
all_walks = []

# Simulate random walk five times
for i in range(5) :

    # Code from before
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
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)

# Print all_walks
print(all_walks)