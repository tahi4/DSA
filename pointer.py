'''
Two Pointers
EASY

1. Valid Palindrome: 

# QUESTION

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

# SOLUTION

1. regular:
take the string
remove all characters that arent ascii
lower case them
match the reverse

2. two pointers:
one ppint at the start of the string
one at the end of string
if the character is not an ascii, keep incrementing
once you react both ascii characters:
check if lowercase them is equivalent 
repeat

'''

# solution 1:

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newSTRING = ''

        for c in s:
            if c.isalnum():
                newSTRING += c.lower()
        return newSTRING == newSTRING[::-1] 
    
# solution 2:

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not self.isAlphaNum(s[l]):
                l += 1
            while r > l and not self.isAlphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


    def isAlphaNum(self, c):
        return (
            ord('A')<=ord(c)<=ord('Z') 
            or  ord('a')<=ord(c)<=ord('z') 
            or  ord('0')<=ord(c)<=ord('9')
             )
            
            

