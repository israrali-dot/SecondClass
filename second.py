import numpy as np

speed = [86,87,88,86,87,85,86]

std_speed = np.std(speed)

print(f"standard deviation of speed is {std_speed}")

speed2 = [32,111,138,28,59,77,97]

std_speed2 = np.std(speed2)

print(f"standard deviation of speed2 is {std_speed2}")

var_speed2 = np.var(speed2)

print(f"varience of speed2 is {var_speed2}")



