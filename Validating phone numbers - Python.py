import re
for _ in range(int(input())):
    if bool(re.match(r'^[7-9]{1}\d{9}$', input())) is True:
        print("YES")
    else:
        print("NO")



"""
Phone nr 
2
9587456281
1252478965
Sample Output
YES
NO
"""