# Website: AlgoExpert: Coding Interview Questions
# Problem: Palindrome Check
# Difficulty: Easy
# https://www.algoexpert.io/questions/Palindrome%20Check


def isPalindrome(string):
    '''
    - O(n^2) time, because incrementing string with one character takes
      O(n) operation to go through all characters and copy to the new
      string
    - O(n) space
    '''
    r_string = ''

    for i in range(len(string) - 1, -1, -1):
        r_string += string[i]

    return string == r_string
