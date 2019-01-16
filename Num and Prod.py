import numpy
"""
my_array = numpy.array([ [1, 2], [3, 4] ])

print(numpy.sum(my_array, axis=0))         # Output : [4 6]
print(numpy.sum(my_array, axis=1))         # Output : [3 7]
print(numpy.sum(my_array, axis=None))      # Output : 10
print(numpy.sum(my_array))                   # Output : 10

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.prod(my_array, axis = 0)            #Output : [3 8]
print numpy.prod(my_array, axis = 1)            #Output : [ 2 12]
print numpy.prod(my_array, axis = None)         #Output : 24
print numpy.prod(my_array)                      #Output : 24
"""
# Leg n en m vast vanuit de 1e input-regel:
n, m = map(int, input().split())
# Elke volgende regel: splits de elementen, zet in list en voeg als int toe en maak een numpy-array:
# Axis is kennelijk de laatste int (=0)
a = numpy.array([input().split() for _ in range(n)], int)
# Eerst numpy.sum van a over as 0; en daarvan numpy.prod over as 0:
print(numpy.prod(numpy.sum(a, axis=0), axis=0))


"""
You are given a 2-D array with dimensions N X M. 
Your task is to perform the sum tool over axis 0 and then find the product of that result.

Input:
2 2
1 2
3 4

Output:
24
"""