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
    

'''

Linked List

EASY
2. Merge Two Sorted Lists:

# QUESTION

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.


Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


# SOLUTION 

iterative:
example: 
list1 = 1 -> 3 -> 4
list2 = 3 -> 5 -> 6

Create a dummy node as a placeholder for the head of the merged list, and set tail to point to it:
dummy -> None
         ^
       tail

In the first iteration of the loop, compare the values of the heads of list1 and list2, which are 1 and 2, respectively. Since 1 is smaller, set tail.next to the node with value 1, and update tail to point to that node:
dummy -> 1 -> None
              ^
            tail

In the second iteration of the loop, compare the values of the heads of list1 and list2, which are now 3 and 2, respectively. Since 2 is smaller, set tail.next to the node with value 2, and update tail to point to that node:
dummy -> 1 -> 2 -> None
                   ^
                 tail

In the third iteration of the loop, compare the values of the heads of list1 and list2, which are now 3 and 5, respectively. Since 3 is smaller, set tail.next to the node with value 3, and update tail to point to that node:
dummy -> 1 -> 2 -> 3 -> None
                        ^
                      tail

etc. etc 

in the case where one list might be longer than the other like =>
list1 = 1 -> 3 -> 4 
list2 = 3 -> 5 -> 6 -> 8 -> 9

bcz its previously sorted, we just need to add it to the list. no further rearrangement requirent

loop ends at: 1 -> 3 -> 3 -> 4 -> None

take the remainder of that list:  5 -> 6 -> 8 -> 9
and assign tail.next to it =  5 -> 6 -> 8 -> 9


'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode() #dummy node
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else: #if equivalent or l2 is smaller
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # if after the loop any list has remaining nodes

        if list1:
            tail.next = list1 

        if list2:
            tail.next = list2 

        return dummy.next #head
    


'''
Linked List

EASY
1. Linked List Cycle:

# QUESTION

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

# SOLUTION

1. hashset: T - O(n) M - O(n) cus using hashmaps
add a node to a hashset after we visit
so if it is a cycle, we will be alerted if a node gets repeated 

2. two pointers + floyds tortoise and hare: T - O(n) M - O(1)

if it is a cycle, 
no matter where the two points are, 
if theyre moving at diff speeds, they'll end up catching up to each other 

create two points slow and fast. slow moves one step, fast moves two. and give them the same starting point
start a while loop according to fast, cus if not cycle, fast will get a null val first
if fast and slow nodes are ever the same its a cycle, else false




'''

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False