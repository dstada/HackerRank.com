def biggerIsGreater(w):
    lst = []

    for letter in w:
        lst.append(ord(letter))
    print(lst)

    # Kijk of het überhaupt groter kan
    # In omgekeerde volgorde sorteren;
    lst_i = sorted(lst, reverse=True)
    if lst == lst_i:        # Volgorde is al maximaal
        return "no answer"

    # van achteraf naar voren kijken waar eerste waarde zit die kleiner is dan rechter buren:
    for i in range(len(w) - 1):
        if lst[len(lst)-i-1] > lst[len(lst) - i - 2]:
            center = lst[len(lst) - i - 2]

            part1 = lst[:len(lst) - i - 2]
            print("part 1: {}".format(part1))

            # Vervang de eerste vanaf rechts waarvan de waarde kleiner is dan rechter buurman,
            right = lst[len(lst) - i - 1:]
            right_ord = sorted(right)
            print("rechter buren oplopend: {}".format(right_ord))
            # Zoek de eerstvolgend qua grootte:
            for value in right_ord:     # begin met laagste, waarde steeds hoger
                if value > center:
                    part2 = [value]   # de waarde die center moet vervangen
                    print("Nieuwe part 2: {}".format(part2))
                    right_ord.remove(value)    # haal de vervanger van center uit right_ord
                    print("Vervanger verwijderd uit rechts: {}".format(right_ord))
                    right_ord.append(center)    # voeg de te vervangen waarde aan rechter deel toe
                    print("Vervangen waarde aan rechts togevoegd: {}".format(sorted(right_ord)))
                    part3 = sorted(right_ord)
                    print("part 3: {}".format(part3))
            print(part1 + part2 + part3)
            return_string = ""
            for part in (part1 + part2 + part3):
                return_string += chr(part)
            print(return_string)
            break       # eerste waarde kleiner dan rechter buur was bereikt: uit de loop


if __name__ == '__main__':
    T = int(input())
    for T_itr in range(T):
        w = input()
        result = biggerIsGreater(w)
        print(result)



"""
Input:
5
ab
bb
hefg
dhck
dkhc

Output:
ba
no answer
hegf
dhkc
hcdk

Output:
6
lmno
dcba
dcbb
abdc
abcd
fedcbabcd

Output:
lmon
no answer
no answer
acbd
abdc
fedcbabdc

https://www.hackerrank.com/challenges/bigger-is-greater/problem?h_r=next-challenge&h_v=zen

for _ in range(int(input())):
    w = input().strip()
    n = len(w)+1
    for k in range(-2,-n,-1):# So I read the word w from right to left,
        if w[k]<w[k+1]:# searching for the first letter w[k] smaller than the previous (from right).
            print(w[:k],end='')# Then I leave the left part of the word unchanged, and print it.
            v = w[:k:-1]# The right part is to be rearranged - inversed first of all - to give the smallest possible.
            for j in range(-k-1):# Then I look for the right place there to insert w[k] which has been found earlier.
                if w[k]<v[j]:# Right place means the leftmost letter v[j] of the inversed right part v, which is greater than w[k].
                    print(v[j]+v[:j]+w[k]+v[j+1:])# Inversion of w[k] and v[j] completes the rearrangement of the right part,
                    break# so I print it and leave.
            else:# If only one (the rightmost) letter of the inversed right part v is greater than w[k], its inversion with w[k]
                print(v+w[k])# means just placing w[k] after the v.
            break
    else:# If no letter of the initial word w is smaller than the previous from right, i.e. the letters are decreasing in the word, 
        print('no answer')# than no rearrangement gives a lexicographically greater.
"""