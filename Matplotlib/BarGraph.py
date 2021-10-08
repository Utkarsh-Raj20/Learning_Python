from matplotlib import pyplot as plt

X = [1,3,5,7,9]
Y = [23,18,31,20,37]

X2 = [2,4,6,8,10]
Y2 = [15,36,28,16,30]

plt.bar(X,Y, label="Company-1",)
plt.bar(X2,Y2, label="Company-2")
plt.title("Income of Companies")
plt.xlabel(" Working Day")
plt.ylabel("Income in Lacks")
plt.legend()
plt.show()