from operator import itemgetter

data = [[1,2,3], [4,5,6], [7,8,9]]


data_new = data.sort(key=itemgetter(1))

print(data_new)