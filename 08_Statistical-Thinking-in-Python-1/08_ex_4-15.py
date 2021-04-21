# Exercise 4-15: Distribution of no-hitters and cycles

import matplotlib.pyplot as plt
from functions import ecdf, successive_poisson

# Draw samples of waiting times: waiting_times
waiting_times = successive_poisson(764, 715, size=100000)

# Make the histogram
plt.hist(waiting_times, bins=100, density=True, histtype='step')

# Label axes
plt.xlabel('waiting time (games)')
plt.ylabel('PDF')

# Show the plot
plt.show()

x, y = ecdf(waiting_times)

# Plot the CDFs and show the plot
plt.plot(x, y, marker='.', linestyle='none')
plt.xlabel('Belmont winning time (sec.)')
plt.ylabel('CDF')
plt.show()
