# Website: AlgoExpert: Coding Interview Questions
# Problem: Palindrome Check
# Difficulty: Easy
# https://www.algoexpert.io/questions/Palindrome%20Check


def isPalindrome(s):
    '''
    :type string: str, 1 <= len(s) <= inf+
    :rtype: boolean, is a string a palindrome?

    Constraints and assumptions:
        - All given characters in string are alphabetic in lowercase.

    e.g. f("abckba") -> abckba == abkcba -> False
    e.g. f("abcdcba") -> abcdcba == abcdcba -> True

    base: s[0] != s[-1] -> False
          len(s) == 0 or 1 -> True
    recursive: s[0] == s[-1], f(s[1:-1])

    Time O(n), where n is len(s)
    Space O(n), where n is len(s)
    '''

    # base cases
    if len(s) == 0 or len(s) == 1:
        return True
    if s[0] != s[-1]:
        return False

    # recursive case
    return isPalindrome(s[1:-1])
