"""
https://www.hackerrank.com/challenges/crossword-puzzle/problem
"""


def crosswordPuzzle(crossword, words):
    vakken = []
    print(crossword)
    print("-------------")
    print(words)
    for i in range(len(crossword)):
        print(crossword[i])
        temp = []
        for j in range(0,10):
            print(crossword[i][j])
            if crossword[i][j] == '-':
                temp.append([i,j])
        print("temp: {}".format(temp))

        if temp != [] and len(temp) > 1:
            print("temp[0][1]: {}".format(temp[0][1]))
            print("temp[0][laatste]: {}".format(temp[len(temp)-1][1]))
            print(temp[len(temp)-1])
            vakken.append(temp)

        # if temp != [] and len(temp) > 1:
        #     vakken.append(temp)
    print(vakken)
    print(len(vakken))


if __name__ == '__main__':
    crossword = []
    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)
    words = input()
    result = crosswordPuzzle(crossword, words)
    # print(result)

"""
Input            
++++++++++
+------+++
+++-++++++
+++-++++++
+++-++-+++
+++-----++
++++++-+++
++++++-+++
++++++-+++
++++++++++
POLAND;LHASA;SPAIN;INDIA

Output:
++++++++++
+POLAND+++
+++H++++++
+++A++++++
+++SPAIN++
+++A++N+++
++++++D+++
++++++I+++
++++++A+++
++++++++++

Input:
+-++++++++
+-++++++++
+-++++++++
+-----++++
+-+++-++++
+-+++-++++
+++++-++++
++------++
+++++-++++
+++++-++++
LONDON;DELHI;ICELAND;ANKARA

Output:
+L++++++++
+O++++++++
+N++++++++
+DELHI++++
+O+++C++++
+N+++E++++
+++++L++++
++ANKARA++
+++++N++++
+++++D++++

Input:
+-++++++++
+-++++++++
+-------++
+-++++++++
+-++++++++
+------+++
+-+++-++++
+++++-++++
+++++-++++
++++++++++
AGRA;NORWAY;ENGLAND;GWALIOR

Output:
+E++++++++
+N++++++++
+GWALIOR++
+L++++++++
+A++++++++
+NORWAY+++
+D+++G++++
+++++R++++
+++++A++++
++++++++++

Input:
XXXXXX-XXX
XX------XX
XXXXXX-XXX
XXXXXX-XXX
XXX------X
XXXXXX-X-X
XXXXXX-X-X
XXXXXXXX-X
XXXXXXXX-X
XXXXXXXX-X
ICELAND;MEXICO;PANAMA;ALMATY

Output:
XXXXXXIXXX
XXMEXICOXX
XXXXXXEXXX
XXXXXXLXXX
XXXPANAMAX
XXXXXXNXLX
XXXXXXDXMX
XXXXXXXXAX
XXXXXXXXTX
XXXXXXXXYX

"""