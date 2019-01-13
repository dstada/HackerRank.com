def separateNumbers(s):     # s is een str
    strings = []
    startcijfers = []
    for i in range(len(s)//2):  # Niet vaker dan de halve lengte van s
        dummy = int(s[0:i+1])   # Startcijfer steeds een cijfer langer
        test = str(dummy)
        teller = 1
        while len(test) < len(s):
            test += str(dummy + teller)
            teller += 1
        strings.append(test)
        startcijfers.append(dummy)
        if s == test:
            break
    if s in strings:
        return_string = "YES " + str(startcijfers[-1:][0])
        return return_string
    else:
        return "NO"




if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        print(separateNumbers(s))

"""
https://www.hackerrank.com/challenges/separate-the-numbers/problem?h_r=next-challenge&h_v=zen
Input:
7
1234
91011
99100
101103
010203
13
1
Output:
YES 1
YES 9
YES 99
NO
NO
NO
NO

4
99910001001
7891011
9899100
999100010001

YES 999
YES 7
YES 98
NO

"""