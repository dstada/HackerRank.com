def pangrams(s):
    alf = "abcdefghijklmnopqrstuvwxyz"
    for letter in s:
        ind = alf.find(letter.lower())
        if ind != -1:
            alf = alf[:ind] + alf[ind + 1:]
    if len(alf) > 0:
        return "not pangram"
    else:
        return "pangram"



if __name__ == '__main__':
    s = input()
    result = pangrams(s)
    print(result)

    """
    https://www.hackerrank.com/challenges/pangrams/problem
    Return pangram if all of the letters of the alphabet are present in the string.
    Input:
    We promptly judged antique ivory buckles for the next prize
    Output: pangram
    Input: We promptly judged antique ivory buckles for the prize
    Output: not pangram
    """