"""Anadrome

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase. For example, "Sool" is an anagram for "Solo".

A palindrome is a word or phrase which reads the same backward as forward, such as "madam".

An anadrome is a word or phrase if any of its anagrams form a palindrome.

For example:
Input: "SoloSolo"
Output: yes ("SoollooS" is an anagram of "SoloSolo" which also is a palindrome).

Input: "3haha"
Output: yes ("ha3ah" is an anagram of "3haha" which also is a palindrome).

Input: "Solo"
Output: no

Write a program to check if the user input is an anadrome or not.

By: Dick Stada - August 2019
"""

word = input("Give word: ").strip()

# Make array with all letters:
word_letters = [letter for letter in word]

# Make set of the unique letters:
word_letter_set = set(word_letters)

# check the  number of occurrences of every unique letter:
odd = 0
ones = 0
for letter in word_letter_set:
    if word_letters.count(letter) % 2 > 0:
        odd += 1
    if word_letters.count(letter) == 1:
        ones += 1
    if odd > 1 or ones > 1:
        print("no")
        break
# Anadrome is each unique letter comes in pairs except for at most 1x
if odd < 2 and ones < 2:
    print("yes")
