def twoStrings(s1, s2):
    # Maak sets en kijk tel de overeenkomstige letters:
    s1s = set(s1)
    s2s = set(s2)
    s1s.intersection_update(s2s)
    if len(s1s) > 0:
        return "YES"
    else:
        return "NO"




if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s1 = input()
        s2 = input()
        result = twoStrings(s1, s2)
        print(result)

"""
2
hello
world
hi
world

Output:
YES
NO

Given two strings, determine if they share a common substring. A substring may be as small as one character.

For example, the words "a", "and", "art" share the common substring a. The words "be" and "cat" do not share a substring."""