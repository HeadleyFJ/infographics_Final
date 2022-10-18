import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
%matplotlib inline


time = [0,1,2,3,4,5,6,7,8,9,10]
cupcakes = [0,1,1,1,2,4,6,6,8,11,12]

plt.scatter(time,cupcakes,c="black",marker='D',s=50)
plt.xlabel('Time in days')
plt.ylabel('Number of cupcakes I have')

plt.show()
