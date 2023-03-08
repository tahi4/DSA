'''
Trees

EASY
1. Invert Binary Tree:

# QUESTION
Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:

Input: root = [2,1,3]
Output: [2,3,1]

Example 3:

Input: root = []
Output: []

# SOLUTION

1. recursive dfs -Depth First Search recursive algorithm to search all the vertices of a tree data structure

        4                                          
      /   \
     7     2
    / \   / \
   9   6 3   1

    --inverse--

        4
      /   \
     2     7
    / \   / \
   1   3 6   9

during the inverse: the left and right subtrees of each node are swapped
The function invertTree() then recursively swaps the left and right subtrees of each node starting from the root
because it calls itself in the function.


'''

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: #no more nodes in the tree to traverse and modify 
            return None
        
        tmp = root.right #2
        root.right = root.left # 2 -> 7
        root.left = tmp # 7 -> 2

        self.invertTree(root.right) # passed as the root parameter to recursively inverse children
        self.invertTree(root.left) ## passed as the root parameter to recursively inverse children

        return root
    

    
'''
Trees

EASY
2. Maximum Depth of Binary Tree:

# QUESTION

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2


# SOLUTION

1. recusrive dfs:

function stops the recursion and returns 0 when it encounters a None node in the binary tree.
else it adds 1, for root node, and then the max value for whichever branch has longest chain
 
        4                                          
      /   \
     7     2
    / \  
   9   6 

maxDepth(root=4) = 1 + max(self.maxDepth(root=7), self.maxDepth(root=2))

--> maxDepth(root=7) = 1 + max(self.maxDepth(root=9), self.maxDepth(root=6))
----> maxDepth(root=9) = 1 + max(0,0) = 1
----> maxDepth(root=2) = 1 + max(0,0) = 1
--> maxDepth(root=7) = 1 + max(1, 1) = 2

maxDepth(root=4) = 1 + max(2, self.maxDepth(root=2))
--> maxDepth(root=2) = 1 + max(0,0) = 1

maxDepth(root=4) = 1 + max(2, 1)
maxDepth(root=4) = 1 + 2 = 3 depth layers (ans)


2. Iterative BFS: The breadth-first search used to search a tree or graph data structure for a node that meets a set of criteria

        4                                          
      /   \
     7     2
    / \  
   9   6 

we create a queue with starting value as 4 queue = [4]
we then take the value root=4 and remove it from queue
and append roots's children queue = [7, 2]
and increment a level

level continues getting incremeneted until no more nodes left to add to queue

3. Iterative DFS:
we create a stack that holds the node, and depth (how far along tree it is) value
while stack isnt empty:
    we take the node and depth value. process it. and remove it from the array
    then we append its children into the array
    and repeat cycle until stack is empty
    depth initially is equivalent to 1, but we increment it to 1 with progression of loop



'''


# solution 1:

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: 
            return 0
        
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left)) # if root node is present
    

from collections import deque

# solution 2:

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = deque()
        if root: # just in case if root it empty
            q = deque([root]) 
        level = 0 # if empty, itll only return 0
        
        while q:
            for i in range(len(q)):

                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                

            level += 1
        
        return level
    
# solution 3
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = [[root, 1]]
        level = 0

        while stack:
            node, depth = stack.pop()

            if node:
                level = max(level, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        
        return level
    


'''
Trees

EASY
3. Diameter of Binary Tree:

# QUESTION

Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:

Input: root = [1,2]
Output: 1

# SOLUTION



'''

    



            
