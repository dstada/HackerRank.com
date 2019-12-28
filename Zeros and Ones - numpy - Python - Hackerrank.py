import numpy

print(numpy.zeros((1,2)))  # type to float

print(numpy.zeros((1,2), dtype = numpy.int)) #Type changes to int

print(numpy.ones((1,2)))                    #Default type is float

print(numpy.ones((1,2), dtype = numpy.int)) #Type changes to int

'''
You are given the shape of the array in the form of space-separated integers, each integer representing the size
of different dimensions, your task is to print an array of the given shape and integer type using the tools
numpy.zeros and numpy.ones.

input:
3 3 3

output:
[[[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]]
[[[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]]
'''
nums = tuple(map(int, input().split()))
print(nums)
print (numpy.zeros(nums, dtype = numpy.int))
print (numpy.ones(nums, dtype = numpy.int))

