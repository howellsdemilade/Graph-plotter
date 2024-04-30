# Graph Plotter

import matplotlib.pyplot as plt

x1 = [2, 4, 5, 6]
y1 = [2, 3, 6, 7]

plt.plot(x1, y1, label = "Line 1")

x2 = [1, 2, 3, 4]
y2 = [1, 2, 4, 4]

plt.plot(x2, y2, label = "Line 2")



plt.xlabel("X axis")

plt.ylabel("Y axis")

plt.title("Demo Graph - Two Lines")

plt.legend()

plt.show()


# Graph Customization

x = [2, 4, 5, 6]
y = [2, 3, 6, 7]

plt.plot(x, y, color = "purple", linestyle = "dashed", linewidth = 4, marker = "o", markerfacecolor = "blue", markersize = 12)

plt.xlim(1, 8)
plt.ylim(1, 8)


plt.xlabel("X axis")

plt.ylabel("Y axis")

plt.title("Demo Graph - Customization")

plt.show()



#Bar Chart

left = [1, 2, 3, 4, 5]
height = [10, 11, 23, 36, 4]

tick_label = ["one", "two", "three", "four", "five"]

plt.bar(left, height, tick_label = tick_label, width = 0.9, color = ["purple", "red"])


plt.xlabel("X axis")

plt.ylabel("Y axis")

plt.title("Demo Graph - Bar Chart")

plt.show()
















