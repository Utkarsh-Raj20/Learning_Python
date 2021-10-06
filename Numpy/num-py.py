import numpy as np

height = np.array([3.5, 5.1, 2.8])
weight = np.array([48, 52, 36.7])

print(weight / height )
print(weight + height)

heightMedian = np.median(height)
heightMean = np.mean(height)
weightMedian = np.median(weight)
weightMean = np.mean(weight)

print(heightMean , heightMedian, weightMean, weightMedian)
