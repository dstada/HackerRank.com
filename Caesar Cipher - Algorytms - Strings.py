def caesarCipher(s, k):
    print(s)
    print(k)
    new_s = ""
    for letter in s:
        # print(ord(letter))
        if 64 < ord(letter) < 91:

            print("Hoofdletter")
        elif 96 < ord(letter) < 123:
            print('Klein')
        else:
            print("Teken")



if __name__ == '__main__':
    n = int(input())
    s = input()
    k = int(input())
    result = caesarCipher(s, k)
    print(result)

"""
    https://www.hackerrank.com/challenges/caesar-cipher-1/problem
    
11
middle-Outz
2

okffng-Qwvb
"""