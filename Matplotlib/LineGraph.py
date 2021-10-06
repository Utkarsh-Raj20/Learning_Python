from matplotlib import pyplot as plt
from matplotlib import style

x = [5, 8, 11, 12]
y = [27, 32, 40, 41]
x2 = [6, 10, 12]
y2 = [30, 36, 42]

plt.plot(x,y,'blue',label = "LineOne",linewidth = 3)
plt.plot(x2,y2,'green',label = "LineTwo",linewidth = 3)
plt.legend()
plt.title("Info")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid(True,color= 'k')

plt.show()