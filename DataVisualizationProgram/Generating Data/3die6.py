import pygal

from die import Die

# Create two D8 dice
die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(6)

# Make some rolls, and store resullts in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
   
# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling 2 D8."
hist.x_labels = []
x_max = die_1.num_sides + die_2.num_sides + die_3.num_sides
for label in range(3, x_max+1):
    hist.x_labels.append(label)

hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('3 D6', frequencies)
hist.render_to_file('3die6 _visual.svg')
