#Matplotlib#1: Plot a line graph showing temperature variations over a week.

import matplotlib.pyplot as plt

days = ["Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri"]

temperatures = [30, 32, 33, 31, 29, 28, 27]

plt.plot(days, temperatures, marker='o', linestyle='-', color='b')

plt.xlabel("Day")
plt.ylabel("Temperature in °C")
plt.title("Temperature Over a Week")

plt.show()