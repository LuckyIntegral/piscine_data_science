''' Tutorial on numpy module '''
import numpy as np # always import numpy as np


# Multidim arrays
matrix = np.array([
    [
        [1,2,3],
        [2,3,4],
    ],
    [
        [2,3,4],
        [3,4,5],
    ],
    [
        [3,4,5],
        [4,5,6],
    ],
    [
        [4,5,6],
        [5,6,7],
    ],
])

print(matrix)
print(matrix[1, 1, -1]) # python feature, same as matrix[1,1,-1]
print(f'matrix.shape: {matrix.shape}') # (4, 2, 3)
print(f'matrix.ndim: {matrix.ndim}') # 3
print(f'matrix[2, 0].ndim: {matrix[2, 0].ndim}') # 1
print(f'matrix.size: {matrix.size}') # 24
print(f'matrix[1].size: {matrix[1].size}') # 6
print(f'matrix.dtype: {matrix.dtype}') # int64

print('\n\n')
print('Filling the arrays')

a = np.full((2,2,2), 0) # memset
print(a)

a = np.zeros((2,2,2)) # bzero
print(a)
print(a.dtype)

a = np.empty((2,2,4)) # alocation only (common for C)
print(a)

x_values = np.arange(0, 1000, 5) # like list from range
print(x_values)

x_values = np.linspace(0, 1000, 21, dtype=np.int64) # distribute into n same pieces
print(x_values)

print('\n\n')
print("Nan and inf")

print(f"np.nan = {np.nan}") # nan
print(f"np.inf = {np.inf}") # inf
print(f"np.isnan(0) = {np.isnan(0)}")           # false
print(f"np.isnan(np.nan) = {np.isnan(np.nan)}") # true
print(f"np.isnan(np.inf) = {np.isnan(np.inf)}") # false

print(f'np.sqrt(-1) = {np.sqrt(-1)}') # nan
print(f'np.isnan(np.sqrt(-1)) = {np.isnan(np.sqrt(-1))}') # complex number is not a number
# print(np.isinf(np.array([10]) / 0)) # gives runtime warning and returns inf

print('\n\n\n')
print('Mathematican operations')

l1 = [1,2,3]
l2 = [4,5,6]

a1 = np.array(l1)
a2 = np.array(l2)

print(f"l1 * 5 = {l1 * 5}") # multiplies elements
print(f"a1 * 5 = {a1 * 5}") # multiplies each element
print(f"np.arange(1, 10) ** 2 = {np.arange(1, 10) ** 2}")
print(f"a1 + a2 = {a1 + a2}")
print(f"a1 * a2 = {a1 * a2}") # if shapes are not the same - error

a1 = np.array([1,2,3])
a2 = np.array([[1,2,3], [4,5,6], [7,8,9]])

print(f'a1 = {a1}')
print(f'a2 = {a2}')
print(f"a1 * a2 = {a1 * a2}") # just aplies the same function to ech pair of elements

a1 = np.array([[1,2,3], [4,5,6]])
print(np.sqrt(a1))

print('\n\n')
print('Array functions')

a = np.array([1,2,3])

print(np.append(a, [4,5,6])) # append() - returns new array with appended values
print(a)

a = np.insert(a, 2, [42,42,42]) # same as append but works by position
print(a)

a = np.array([[1,2,3], [4,5,6]])
print(f'a = {a}')
# print(f"np.delete(a, 1) = {np.delete(a, 1)}") - is getting weird
print(f"np.delete(a, 0, 0) = {np.delete(a, 1, 1)}")

print(a.shape)
print(a.reshape((3, 2))) # well really weird
print(a.reshape((1, 6))) # well really weird
print(a.reshape((6, 1))) # ok, makes scense

a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(a.reshape((2,2,3))) # ok, makes scense
a.resize(6,2) # modifies the array, doesnt create a new one
print(a)

print(f'ravel   = {a.ravel()} however returns a new one') # reshapes into 1 dim array
print(a)
print(f'flatten = {a.flatten()} returns the same one that is flatter (shallow copy)')
print(a)

var = [v for v in a.flat]
print(var)

a = np.array([[1,2,3],
     [4,5,6],
     [7,8,9]])
print(a)
print(a.transpose())

a = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(a.flatten())
print(a.T.flatten())

print('\n\n\n')
print("Concats of arrays ans so on")

a1 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
a2 = np.array([[11,12,13,14,15], [16,17,18,19,20]])

print('Two ways of adding arrays:')
print(f'1: concatenate - {np.concatenate((a1, a2), axis=1)}')
print(f'2: stack - {np.stack((a1, a2))}')
print('Once stack() is about adding one array on top of another, concatenate() is more flexable')

a1 = np.array([[1,2,3,4,5,6], [7,8,9,10,11,12]])

print(np.split(a1, 6, axis=1))

print(np.split(np.arange(100), 2))
a1 = a1.flatten()
print()
print(a1)
print(f"a1.min() = {a1.min()}")
print(f"a1.max() = {a1.max()}")
print(f"a1.mean() = {a1.mean()}")
print(f"a1.std() = {a1.std()}")
print(F"a1.sum() = {a1.sum()}")
print(F"np.median(a1) = {np.median(a1)}")

print('\n\n\n')
print("Random generator")
# first two for radius, size for the shape
print(np.random.randint(90, 100, size=(2,3,4)))
# well, as result we have shape 5/10 with values of binomial distributions
# binomial - close to centrum
print(np.random.binomial(10, p=0.5, size=(5, 10)))
#
print(np.random.choice([2,4,6,8,10,12,14,16,18,20], size=10))


print('\n\n\n')
print("Export/import files")

print('using save: saves to npy format')
np.save('myarray.npy', a)
a = np.load('myarray.npy')
print(a)

print('saves to whatever you want')
sp = a.shape
a = a.flatten()
np.savetxt('aplication.csv', a, delimiter=',')
a = np.loadtxt('aplication.csv', delimiter=',')
a.resize(sp)
print(a)
