import re

m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
print(m.group(0))       # The entire match

print(m.group(1))       # The first parenthesized subgroup

print(m.group(2))      # The second parenthesized subgroup

print(m.group(3))       # The third parenthesized subgroup

print(m.group(1,2,3))   # Multiple arguments give us a tuple

print(m.groups())

m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
print(m.groupdict())

m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
print(m.group(1) if m else -1)

# input: ..12345678910111213141516171820212223
# output: 1