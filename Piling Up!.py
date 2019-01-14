from collections import deque
for _ in (range(int(input()))):
    input()
    side_lengths = list(map(int, input().strip().split()))
    result = "Yes"
    if max(side_lengths) not in (side_lengths[0], side_lengths[-1]):
        result = "No"
    print(result)


"""
from collections import deque
    
    
for _ in (range(int(input()))):
    input()
    side_lengths = deque(map(int, input().strip().split()))
    result = "Yes"
    if max(side_lengths) not in (side_lengths[0], side_lengths[-1]):
        result = "No"
    print(result)

    
2
6
4 3 2 1 3 4
3
1 3 2

Outut:
Yes
No
"""