def biggerIsGreater(w):
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
            center = lst[len(lst) - i - 2]

            print("rechter buren: {}".format(lst[len(lst) - i - 1:]))
            rest_lst = sorted(lst[len(lst) - i - 1:])
            print("rest_lst: {}".format(rest_lst))

            part1 = lst[:len(lst) - i - 2]
            print("part 1: {}".format(lst[:len(lst) - i - 2]))

            # Dus: 1) vervang de eerste vanaf rechts waarvan de waarde kleiner is dan rechter buurman,
            right = lst[len(lst) - i - 1:]
            right_ord = sorted(right)
            print(right_ord)
            # Zoek de eerstvolgend qua grootte:
            for value in right_ord:
                if value > center:
                    part2 = value   #
                    print(part2)
                    right_ord.remove(value)    # haal de vervanger van center uit right_ord
                    print(right_ord)
                    right_ord.append(center)    # voeg de te vervangen waarde aan rechter deel toe
                    print(sorted(right_ord))


            # door de kleinste van de rechter buurmannen en zet de rest in oplopende volgorde.
            break


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