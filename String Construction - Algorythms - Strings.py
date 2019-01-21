def stringConstruction(s):
    return(len(set(s)))



if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = stringConstruction(s)
        print(result)


"""
2
abcd
abab

Output
4
2
"""