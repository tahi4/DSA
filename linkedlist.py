'''
Linked List

EASY
1. Reverse Linked List:

# QUESTION

Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []

# SOLUTION

1. iterative + two pointers:

5 -> 3 -> 4 -> None
currently, 5 is the head, and 4 is the end facing null

so if we were to reverse this list 4 would be head while 5 would be the last facing null
4 -> 3 -> 5 -> None  # result we'd like to achieve 

5 -> 3 -> 4 -> None
lets start by facing 5 to None, we can do this by using pointers
set a previous pointer to none, and the current to the head (5)
once we do this: None <- 5  3 -> 4 -> None
change the previous value to 5, and current to 3 and change what its facing None <- 5 <- 3  4 -> None
repeat the process, until the current value is null
then the previous value at the end of the loop should be our NEW HEAD

test


'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        prev, current = None, head
        while current:
            nxt = current.next #before we break the bond we need to store it temporarily, to update the new current value
            current.next = prev
            prev = current
            current = nxt
        return prev
    

