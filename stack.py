'''
Stack
EASY
1. Valid Parentheses:

# QUESTION

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

# SOLUTION

1. hashmap + stack:
so we use a hasmap to assign a closed bracked with an open bracket '}' : '{'
then we make a list, that only includes open brackets,
so when we come across our first closed bracket, 
we match it up with the last index inside the stacks array, and see if it matches
if it does, we remove the last array and move on,
finally, if the stack is empty: we return true


'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        hashmap = {'}': '{', ']': '[', ')': '('}

        # look for closing brackets in string
        for c in s:
            if c in hashmap:
                if stack and stack[-1] == hashmap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False  #if the stack is empty return true

        

