import numpy as np  

#creating array from scratch

zeros = np.zeros((3,4))
print("Zeros array: \n",zeros)

ones = np.ones((3,4))
print("Ones array: \n",ones)

full = np.full((2,2), 7)
print("Full array: \n",full)

random = np.random.random((2,3))
print("Random array: \n",random)

sequence = np.arange(0,11,2)
print("Sequence array: \n",sequence)
