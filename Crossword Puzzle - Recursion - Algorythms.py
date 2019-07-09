"""https://www.hackerrank.com/challenges/crossword-puzzle/problem
"""


def crosswordPuzzle(crossword, words):
    vakken = []
    print(crossword)
    print("-------------")
    print(words)
    woorden = words.split(";")
    print(woorden)
    for i in range(len(woorden)):
        print(woorden[i])

    # Horizontale woordvakken bepalen:
    for i in range(len(crossword)):
        # print(crossword[i])
        temp = []
        for j in range(0,10):
            # print(crossword[i][j])
            if crossword[i][j] == '-':
                temp.append([i,j])
        if temp != [] and len(temp) > 1:
            # Cellen moeten aansluitend zijn, anders kan er geen woord in:
            if len(temp) == temp[len(temp)-1][1] - temp[0][1] + 1:
                vakken.append(temp)
    print(vakken)

    # Verticale woordvakken bepalen:
    for k in range(0,10):   # Voor elke kolom
        temp2 = []
        word = 0
        for l in range(0,10):
            if crossword[l][k] == '-':      # invulvakje en niet het laatste vakje
                word += 1                   # leeg invulvakje
                temp2.append([l,k])
                if l == 9 and word > 1:
                    vakken.append(temp2)
                    temp2 = []
                    word = 0
            else:                           # geen leeg vakje
                if word > 1:                # als er al eerder ruimte voor een woord was, dan wegschrijven in temp2
                    vakken.append(temp2)    # tijdelijke lege vakken toevoegen aan vakken
                temp2 = []              # temp2 weer leegmaken
                word = 0                # teller weer op 0 voor evt. volgend woord
        print(temp2)
    print(vakken)
    for x in vakken:    # print elk invulvak uit vakken:
        print(x)
        print(len(x))
        for word in woorden:
            print(word)
            if len(word) == len(x):
                print("gelijk!")
                break
            else:
                print("NIET gelijk!")


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