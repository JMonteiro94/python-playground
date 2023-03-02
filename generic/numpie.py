import numpy as np
import numpy.linalg as la


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

a = np.round(10 * np.random.rand(5, 4))
a_value_in_row_1_col_2 = a[1, 2]
a_all_rows_first_col = a[:,1]
a_sub_matrix = a[1:3, 2:4]
#a_index_array = a[[1, 4, 5]]
a_value_less_than_8 = a[a < 8]

la.inv(np.random.rand(3, 3))

B = np.arange(100)
print(B[(B<40) & (B>10)])

matrix_2_by_3 = np.round(10 * np.random.rand(2,3))
matrix_2_by_3 = matrix_2_by_3 + 3
matrix_2_by_3 = matrix_2_by_3 + (np.arange(2).reshape(2,1))
B = np.round(10 * np.random.rand(2, 2))
C = np.hstack((matrix_2_by_3, B))
A = np.random.permutation(np.arange(10))
print(A)
print(np.sort(A))
print(np.sort(A))

A = np.array(["abs", 'how are you', 'u765', '13er'])
A.sort()

b = np.random.rand(1000000)
