import numpy as np
import matplotlib.pyplot as plt

# importing the parameter file
try:
    with open('data.txt') as f:
        lines = f.readlines()
except FileNotFoundError:
    print("The file was not found")

# creating a dictonary with the parameters
params = {}
for param in lines:
    splitedS = param.split()
    params[splitedS[0]] = splitedS[1]

# generating random numbers
np.random.seed(12424)

if params["distributionType"] == 'g':
    numbers = float(params["widthSDFraction"]) * np.random.randn(int(params["totalNTries"]))
else:
    print(f"{params['distributionType']} is an unknown distribution type")
    
# computing the histogram
hist, bin_edges = np.histogram(numbers, bins=int(params["nBins"]))

# plotting the histogram
plt.hist(bin_edges[:-1], bin_edges, weights=hist)
plt.show()
