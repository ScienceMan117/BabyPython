import matplotlib.pyplot as plt

x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]

""" Defining custom colors by name or setting the RGB color model """
# plt.scatter(x_values, y_values, c=(0.7, 0.5, 0.8), edgecolor='none', s=40)

""" Using a colormap used in visualizations to emphasize a pattern in the data.
"""
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds,
            edgecolor='none', s=40)

# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=12)
plt.ylabel("Square of Value", fontsize=12)


# Set the range for each axis, including the minimum and maximum for the x and 
# y axis
plt.axis([0,6000,0,150000000000])

plt.show()

"""Automatically saves the plot to a file, replace the below code with the code
above. THe first arugment is a filename for the plot image, which will be saved
in the same directory as scatter_squares.py The second argument trims extra
whitespace around the polt, you can omit this argument.(Python Crash Course,
Pg. 331"""
# plt.savefig('squares_plot.png', bbox_inches='tight')
