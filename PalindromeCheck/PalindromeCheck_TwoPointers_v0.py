def isPalindrome(string):
    '''
    :type string: str, 1 <= len(s) <= inf+
    :rtype: boolean, is string a palindrome?

    Ways to solve:
        - use a built-in reverse() and compare to a given string
            - O(n) time, O(n) space
        - make your own reverse a string function
            - O(n) time, O(n) space
        - compare first and last letter of a string (recursively)
            - O(n) time, O(n) space
        - compare first and last letter of a string (iteratively)
            - O(n) time, O(1) space

    f('a') -> True
    f('abc') -> False
    f('abcdcba') -> True
    '''

    for i in range(len(string) // 2):
        # check if chars from left and right are the same
        if string[i] != string[-i - 1]:
            return False
    return True
