

def highestValuePalindrome(s, n, k):
    new_s = ""
    changes = 0
    if n % 2 != 0:
        center = s[len(s)//2]
    else:
        center = ""
    for i in range(len(s)//2):
        if str(s[i:i+1]) != str(s[len(s)-1-i:len(s)-i]):
            new_s +=str(max(s[i:i+1], s[len(s)-1-i:len(s)-i]))
            changes += 1
        else:
            new_s += str(s[i:i+1])
    if changes > k:
        return "-1"
    else:
        new_s = new_s + center + new_s[::-1]
        return new_s


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    s = input()
    result = highestValuePalindrome(s, n, k)
    print(result)


"""
https://www.hackerrank.com/challenges/richie-rich/problem

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