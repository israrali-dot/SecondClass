import numpy as np

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
speed_mean = np.mean(speed)
print("The mean of speed feature is ",speed_mean)
speed_median = np.median(speed)
print("The median of speed feature is ",speed_median)

from scipy import stats
speed_mode = stats.mode(speed)
print("The mode of speed feature is ",speed_mode)


