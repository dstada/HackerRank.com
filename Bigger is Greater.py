def biggerIsGreater(w):
    print(w)
    lst = []

    for letter in w:
        lst.append(ord(letter))
    print(lst)

    # Kijk of het groter kan
    # In omgekeerde volgorde sorteren;
    lst_i = sorted(lst, reverse=True)
    if lst == lst_i:
        return "no answer"

    # van achteraf naar voren kijken waar eerste waarde zit die kleiner is dan rechter buren:
    for i in range(len(w) - 1):
        if lst[len(lst)-i-1] > lst[len(lst) - i - 2]:
            print("Rechter buurman van {} groter!".format(lst[len(lst) - i - 2]))
            print("rechter buren: {}".format(lst[len(lst) - i - 1:]))
            print("Deze waarde(s) blijft/blijven staan: {}".format(lst[:len(lst) - i - 1]))

            # Dus: 1) vervang de eerste vanaf rechts waarvan de waarde kleiner is dan rechter buurman,
            # door de kleinste van de rechter buurmannen en zet de rest in oplopende volgorde.

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


https://www.hackerrank.com/challenges/bigger-is-greater/problem?h_r=next-challenge&h_v=zen
"""