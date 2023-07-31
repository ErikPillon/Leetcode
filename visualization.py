import matplotlib.pyplot as plt
import numpy as np
import os



# Create a bar chart showing the number of Python files solved over time
plt.bar(data[:, 0], data[:, 1], label="Number of Python files")
plt.xlabel("Time")
plt.ylabel("Number of Python files")
plt.title("Number of Python files solved over time")
plt.legend()

# Save the bar chart
plt.savefig("bar_chart.png")

# Create a pie chart showing the distribution of LeetCode problems solved
plt.pie(data[:, 2], labels=data[:, 3], autopct="%1.1f%%")
plt.title("Distribution of LeetCode problems solved")
plt.savefig("pie_chart.png")

# Create a scatter plot showing the relationship between the number of lines of code and the percentage of files that pass all test cases
plt.scatter(data[:, 4], data[:, 5])
plt.xlabel("Number of lines of code")
plt.ylabel("Percentage of files that pass all test cases")
plt.title("Relationship between number of lines of code and percentage of files that pass all test cases")
plt.savefig("scatter_plot.png")