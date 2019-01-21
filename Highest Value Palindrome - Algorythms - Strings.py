def highestValuePalindrome(s, n, k):
    print(s, n, k)
    # Vergelijk steeds de buitensten en dan naar binnen:
    print(str(s[:1]), str(s[len(s)-1:len(s)]))
    print(str(s[1:2]), str(s[len(s)-2:len(s)-1]))


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    s = input()
    result = highestValuePalindrome(s, n, k)
    print(result)


"""
4 1
3943
Sample Output 
3993

Sample Input
6 3
092282
Sample Output
992299

Sample Input 
4 1
0011
Sample Output
-1
"""