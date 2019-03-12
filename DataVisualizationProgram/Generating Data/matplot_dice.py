import numpy as np
import matplotlib.pyplot as plt

from die import Die

# Create two D6 dice
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(5000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
    
# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides

x_max = die_1.num_sides + die_2.num_sides

plt.hist(results, bins=np.arange(2, max_result+2)-.5, histtype = 'bar', 
         rwidth=0.8, facecolor = 'blue', edgecolor="k")

plt.title("Dice Plot")
plt.xlabel("Results")
plt.ylabel("Frequency of Result")

plt.show()


