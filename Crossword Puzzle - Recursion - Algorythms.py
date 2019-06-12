
import os


def crosswordPuzzle(crossword, words):
    print(crossword)
    print("-------------")
    print(words)
    for i in range(len(crossword)):
        print(crossword[i])
        for j in range(0,11):



if __name__ == '__main__':
    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    words = input()

    result = crosswordPuzzle(crossword, words)
    print(result)

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

"""