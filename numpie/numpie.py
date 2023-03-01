import numpy as np


a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
a = np.array([[1, 2, 3, 4, 5, 6]], dtype='i')
print(a)
f = np.array([[1, 2, 3, 4, 5, 6]], dtype='f')
print(f)
b = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(b)
print(b.shape)
print(b.ndim)
print(b.shape[0], b.shape[1], b.shape[2])
print(b[1, 0, 2])
print(b.dtype)

