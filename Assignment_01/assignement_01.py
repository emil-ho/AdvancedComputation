import numpy as np
import matplotlib.pyplot as plt

# importing the parameter file
with open('data.txt') as f:
    lines = f.readlines()

# creating a dictonary with the parameters
params = {}
for param in lines:
    splitedS = param.split()
    params[splitedS[0]] = splitedS[1]

# generating random numbers and creating the histogram
np.random.seed(12424)

if params["distributionType"] == 'g':
    numbers = np.random.randn(int(params["totalNTries"]))
    rnge = (- 1 / float(params["widthSDFraction"]), 1 / float(params["widthSDFraction"]))
    hist, bin_edges = np.histogram(numbers, bins=int(params["nBins"]))
    
elif params['distributionType'] == 'u':
    numbers = np.random.rand(int(params["totalNTries"]))
    hist, bin_edges = np.histogram(numbers, bins=int(params["nBins"]))
     
else:
    print(f"{params['distributionType']} is an unknown distribution type")

# plotting the histogram
plt.hist(bin_edges[:-1], bin_edges, weights=hist)
plt.xlabel("value")
plt.ylabel("occurence")
plt.title("random value distribution")
plt.savefig('histogram.jpg')
plt.show()
