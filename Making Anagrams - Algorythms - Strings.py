def makingAnagrams(s1, s2):
    s1l = [letter for letter in s1]
    s2l = [letter for letter in s2]
    for letter in s1:
        if s2l.count(letter) > 0:
            s1l.remove(letter)
            s2l.remove(letter)
    return len(s1l) + len(s2l)


if __name__ == '__main__':
    s1 = input()
    s2 = input()
    result = makingAnagrams(s1, s2)
    print(result)

"""
cde
abc

Output: 4"""