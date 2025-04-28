import numpy as np

# Vector,Matrix and Tensor

vector = np.array([1,2,3,4,5])
print("Vector:",vector)

matrix = np.array([[1,2,3],[4,5,6]])
print("Matrix:",matrix)

tensor = np.array([[[1,2,3],[4,5,6]],
                   [[7,8,9],[3,5,7]]])
print("Tensor:",tensor)

#array properties

arr = np.array([[1,2,3],
                [4,5,6]])
print("Shaper ",arr.shape)
print("Dimension ",arr.ndim)
print("Size ",arr.size)
print("DType ",arr.dtype)

#array Reshaping

arr = np.arange(12)
print("Original array",arr)

reshaped = arr.reshape((3,4))
print("Reshaped array",reshaped)

flattened = reshaped.flatten()
print("Flattened array",flattened)

#ravel (returns view,instead of copy)
reveled = reshaped.ravel()
print("Reveled array",reveled)

#transpose
transpose = reshaped.T
print("Transpose array",transpose)