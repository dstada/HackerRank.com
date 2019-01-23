def caesarCipher(s, k):
    print(s)
    print(k)
    new_s = ""
    for letter in s:
        # print(ord(letter))
        new_letter = ""
        if 64 < ord(letter) < 91:       # Hoofdletter
            if ord(letter) + k > 90:
                new_letter = chr(ord(letter) + k - 26)
            else:
                new_letter = chr(ord(letter) + k)
        elif 96 < ord(letter) < 123:            # Kleine letter
            if ord(letter) + k > 122:
                new_letter = chr(ord(letter) + k - 26)
            else:
                new_letter = chr(ord(letter) + k)
        else:                           # Geen kleine of hoofdletter
            new_letter = letter     # Niets veranderen aan de input-letter
        new_s += new_letter
    print(new_s)




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

36
There's-a-starman-waiting-in-the-sky
3
"""