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
plt.xlabel("value")
plt.ylabel("occurence")
plt.title("random value distribution")
plt.show()

#NEW CODE

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
   
# computing the histogram   
    hist, bin_edges = np.histogram(numbers, bins=int(params["nBins"]))

# plotting the histogram   
    plt.hist(bin_edges[:-1], bin_edges, weights=hist)
    plt.show()
    
else:
    if params["distributionType"] == 'u':
        
 # generating random numbers 
        numbers = np.random.randn(int(params["totalNTries"])) 
        
# computing the histogram        
        count, bins, ignored = plt.hist(numbers,bins=int(params["nBins"],density=True)) 
        
# plotting the histogram        
        plt.plot(bins, np.ones_like(bins), linewidth=1, color='r')
        plt.show()
    else:
        print(f"{params['distributionType']} is an unknown distribution type")
