import numpy as np

## Datatype and Attributes

# Numpy's main datatype is nparray

a1 = np.array([1, 2, 3])
a1

type(a1)

a2 = np.array([[1, 2, 3],
               [4, 5, 6.5]])

a3 = np.array([[[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]],
              [[10, 11, 12],
               [13, 14, 15],
               [16, 17, 18]]])

a2

a3

type(a2)

type(a3)

a1.shape

a2.shape

a3.shape

a1.ndim, a2.ndim, a3.ndim

 a1.dtype, a2.dtype, a3.dtype

a1.size, a2.size, a3.size

type(a1), type(a2), type(a3)

a2

# create a Dataframe from a NumPy array

import pandas as pd

df = pd.DataFrame(a2)
df

## 2. Creating arrays

sample_array = np.array([1, 2, 3])
sample_array 

sample_array.dtype

ones = np.ones((2, 3))

ones

ones.dtype

type(ones)

zeros = np.zeros((2, 3))

zeros

range_array = np.arange(0, 10, 2)
range_array

random_array = np.random.randint(0, 10, size =  (3, 5))

random_array

random_array.size

random_array.shape

random_array_2 = np.random.random((5, 3))

random_array_2

random_array_2.shape

random_array_3 = np.random.rand(5,3)
random_array_3

# Pseudo-random numbers

np.random.seed(seed = 99999)

random_array_4 = np.random.randint(10, size = (5,3))
random_array_4


np.random.seed(seed = 7)
random_array_5 = np.random.random((5,3))
random_array_5

random_array_5 = np.random.random((5, 3))
random_array_5

random_array_4

## 3. Viewing arrays and matrices

np.unique(random_array_4)

a1

a2

a3

 a1[0]

a2.shape

a2[0]

a3.shape

a3

a3[0]

a2

a2[1]

a3

a3[:]

a3[:2, :2, :2]

a4 = np.random.randint(10, size = (2, 3, 4, 5))
a4

a4.shape, a4.ndim

# Get the first 4 number of the inner most arrays
a4[:, :, :, :3]

a4[:, :, :, :4]

a4[:, :, :, :1]

## 4. Manipulating & comparing arrays

## Arithmetic

a1 

ones = np.ones(3)
ones

a1 + ones

a1 - ones

a1 * ones

a1

a2 

a1 * a2

a3

# How to you reshape a2 to be compatible with a3?
# Search:" How to reshape numpy array"
#a2 * a3   #ValueError: operands could not be broadcast together with shapes (2,3) (2,3,3) 


a1 / ones

a2 / a1

a2 // a1

# Floor division removes the decimals(rounds down)
a2 // a1

a2

a2 ** 2

np.square(a2)

np.add(a1, ones)

a1 + ones

a1 % 2

a1 / 2

a2 % 2

np.exp(a1)

np.log(a1)

### Aggregation 

Aggregation = Performing the same operation on a number of things

listy_list = [1, 2, 3]
type(listy_list)

sum(listy_list)

a1

sum(a1)

np.sum(listy_list)

 Use Pyhton's methods ( sum() ) on Python datatype and use Numpy's methods on NumPy arrays (np.sum() )

 # Creative a massive NumPy array
massive_array = np.random.random(100000)
massive_array

massive_array.size

massive_array[:100]

massive_array[:10]

%timeit sum(massive_array)  #Python's sum()
%timeit np.sum(massive_array)  #NumPy's sum()

a2

np.mean(a2)

np.max(a2)

# Standard Deviation = a measure of how spread out a group of number is from the mean
np.std(a2)

# Variance = measure of the average degree to which each number is different to the mean
# Higher variance = wider range of numbers
# Lower variance = lower range of numbers
np.var(a2)

# Standard Deviation = squareroot of variance
np.sqrt(np.var(a2))

# DEmo of std and var
high_var_array = np.array([1, 100, 200, 300, 4000, 5000])
low_var_array = np.array ([ 2, 4, 6, 8, 10 ])

np.var(high_var_array), np.var(low_var_array)

np.std(high_var_array), np.std(low_var_array)

np.mean(high_var_array), np.mean(low_var_array)

%matplotlib inline
import matplotlib.pyplot as plt
plt.hist(high_var_array)
plt.show()

plt.hist(low_var_array)
plt.show()

## Reshaping & Transposing

a2

a2.shape

 a3

a3.shape

a2.shape

a2.reshape(2, 3, 1)

a2.reshape(2, 3, 1).shape

a3.shape

a2_reshape = a2.reshape(2, 3, 1)
a2_reshape

a2_reshape * a3

# Transpose = switches the axis
a2.T

a2.shape

a2.T.shape

a3.shape

a3.T

a3.T.shape

## Dot Product

np.random.seed(0)

mat1 = np.random.randint(10, size = (5, 3))
mat2 = np.random.randint(10, size = (5, 3))

mat1

mat2

mat1.shape, mat2.shape

# Element-wise multiplication (hadamard product)
mat1 * mat2

#np.dot(mat1, mat2)  #ValueError: shapes (5,3) and (5,3) not aligned: 3 (dim 1) != 5 (dim 0)


# Transpose mat1
mat1.T

mat1.T.shape

mat2.T

mat2.T.shape

mat1.shape, mat2.T.shape

mat3 = np.dot(mat1, mat2.T)
mat3

mat3.shape

## Dot product example(nut butter sales)

np.random.seed(0)

# Number of jars sold
sales_amounts = np.random.randint(20, size = (5, 3))
sales_amounts

# cretae weekly_sales DataFrame
weekly_sales = pd.DataFrame(sales_amounts, 
                            index = ["Mon", "Tues", "Wed", "Thur", "Fri"],
                           columns = ["Almond butter", "Peanut butter", "Cashew butter"])
weekly_sales

# Create prices array
prices = np.array ([10, 8, 12])
prices

prices.shape

# create butter_prices DataFrame
butter_prices = pd.DataFrame(prices.reshape(1,3),
                            index = ["prices"],
                            columns = ["Almond butter", "Peanut butter", "cashew butter"])
butter_prices

# total_sales = prices.dot(sales_amounts)  # shapes  not aligned

# let's transpose
total_sales = prices.dot(sales_amounts.T)
total_sales

# cretae daily_sales
butter_prices

weekly_sales

butter_prices.shape, weekly_sales.shape

weekly_sales.T.shape

#daily_sales = butter_prices.dot(weekly_sales.T)  #ValueError: matrices are not aligned


#weekly_sales["Total ($)"] = daily_sales.T
#weekly_sales

### Comparison operator

a1

a2

a1 > a2

bool_array = a1 >= a2
bool_array

type(bool_array), bool_array.dtype

a1 > 5

a1 < 5

a1 == a1

a1 == a2

## 5. Sorting arrays

random_array

random_array = np.random.randint(10, size = (3,5))
random_array

random_array.shape

np.sort(random_array)

random_array

np.argsort(random_array)

a1 

np.argsort(a1)

np.argmin(a1)

np.argmax(a1)

np.argmin(random_array)

np.argmax(random_array)

np.argmax(random_array, axis = 0)

np.argmax(random_array, axis = 1)

## 6. Practical Example - Numpy in Action!!!

<img src="images/panda.png"/>

# Turn an image into a Numpy array
from matplotlib.image import imread

panda = imread("images/panda.png")
print(type(panda))

panda

panda.size, panda.shape, panda.ndim

panda[:100]

panda[:5]

<img src="images/car-photo.png"/>

car = imread("images/car-photo.png")
print(type(car))

car

car[:1]

<img src="images/dog-photo.png"/>

dog = imread("images/dog-photo.png")
print(type(dog))

dog

dog[:1]

