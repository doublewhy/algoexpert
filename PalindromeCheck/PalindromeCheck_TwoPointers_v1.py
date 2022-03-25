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
    leftP = 0
    rightP = len(string) - 1

    while leftP <= rightP:
        # check if chars from left and right are the same
        if string[leftP] != string[rightP]:
            return False
        leftP += 1
        rightP -= 1

    return True
