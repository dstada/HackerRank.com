def insertion_sort(l):
    for i in range(0, len(l)):
        j = i-1                 # j wordt een eerder dan i (begint bij l[0]
        key = l[i]              # key wordt eerst het 2e cijfer
        while (j >= 0) and (l[j] > key):     # Zolang j>0 (dus niet de eerste ronde, en l[j] groter dan key:
           l[j+1] = l[j]        # l[j] schuift naar rechts
           j -= 1               #
        l[j+1] = key            #

m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))


"""
https://www.hackerrank.com/challenges/correctness-invariant/forum

Input:

6
7 4 3 5 6 2

Output: 2 3 4 5 6 7
"""