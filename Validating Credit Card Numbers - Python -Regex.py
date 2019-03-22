import re


for _ in range(int(input())):
    if bool(re.match(r'^[4-6]{1}[\d]{3}[-|\s]?[\d]{4}[-|\s]?[\d]{4}[-|\s]?[\d]{4}$', input())) is True:
        print("Valid")
    else:
        print("Invalid")



"""

► It must start with a 4, 5 or 6. 
► It must contain exactly 16 digits. 
► It must only consist of 0-9 digits (). 
► It may have digits in groups of 4, separated by one hyphen "-". 
► It must NOT use any other separator like ' ' , '_', etc. 
► It must NOT have 4 or more consecutive repeated digits.

Input:
6
4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367-8912-3456
5123 - 3567 - 8912 - 3456

Output:
Valid
Valid
Invalid
Valid
Invalid
Invalid

https://www.hackerrank.com/challenges/validating-credit-card-number/problem?h_r=next-challenge&h_v=zen
"""