n, x = map(int, input().split())
results = []
for _ in range(x):      # Voor elke student doen:
    results.append(list(map(float, input().split())))

res2 = list(zip(*results))
for one in res2:
    print(sum(one)/len(one))

"""
input:
5 3
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5

output:
90.0 
91.0 
82.0 
90.0 
85.5  

>>> print zip([1,2,3,4,5,6],'Hacker')
[(1, 'H'), (2, 'a'), (3, 'c'), (4, 'k'), (5, 'e'), (6, 'r')]
>>> 
>>> print zip([1,2,3,4,5,6],[0,9,8,7,6,5,4,3,2,1])
[(1, 0), (2, 9), (3, 8), (4, 7), (5, 6), (6, 5)]
>>> 
>>> A = [1,2,3]
>>> B = [6,5,4]
>>> C = [7,8,9]
>>> X = [A] + [B] + [C]
>>> 
>>> print zip(*X)
[(1, 6, 7), (2, 5, 8), (3, 4, 9)]
"""