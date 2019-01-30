def commonChild(s1, s2):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

"""
https://www.hackerrank.com/challenges/common-child/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings&h_r=next-challenge&h_v=zen

Input:
HARR
SALLY

Output: 2

Input:
AA
BB
Output: 0

Input:
SHINCHAN
NOHARAAA

Output: 3

Input:
ABCDEF
FBDAMN

Output:
2
"""