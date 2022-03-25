# Website: AlgoExpert: Coding Interview Questions
# Problem: Palindrome Check
# Difficulty: Easy
# https://www.algoexpert.io/questions/Palindrome%20Check


def isPalindrome(string):
    '''
    - O(n) time, O(n) space
    '''
    r_string = []

    for i in range(len(string) - 1, -1, -1):
        r_string.append(string[i])

    return string == "".join(r_string)
