def hackerrankInString(test_string):
    hw = "hackerrank"
    outpt = ""
    # pak letter voor letter uit s en check of dat in de hw-string zit
    if len(test_string) < len(hw):    # Als s korter is dan hw kan hw nooit in s zitten.
        return "NO"
    else:
        for letter in hw:       # Voor elke letter van hackerrank:
            for i in range(len(test_string)):
                if letter == test_string[i]:
                    outpt += letter
                    test_string = test_string[i + 1:]
                    break
        if outpt == hw:
            return "YES"
        else:
            return "NO"





if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        # fptr.write(result + '\n')
        print(result)

"""
2
hereiamstackerrank
hackerworld

Output:
YES
NO
-------------
2
hhaacckkekraraannk
rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt

YES
NO
"""