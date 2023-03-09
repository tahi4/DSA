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

height(node in binary tree) = 1 + max(height(node.left), height(node.right))#HEIGHT IS EQUIVALENT TO THE MAX HEIGHT OF EITHER SIDE  #add 1 to that value to get the height of the current node
Diameter of a binary tree:  max height left subtree + max height of right subtree

height of a leaf node is defined to be 1,  leaf node is a node that is at the end of a branch and has no further nodes connected to it.

recursive dfs:



        4                                          
      /   
     7     
    / \  
   9   6 
  /      \  
8         5 

FINDING BOTTOM MOST NODE

height of root node=4 => 1 + max(node 7, 0)
-> height of root node=7 => 1 + max(node 9,node 6)
--> height of root node=9 => 1 + max(node 8, 0) ---> height of root node=8 => 1 + max(0, 0)
--> height of root node=6 => 1 + max(node 5, 0) ---> height of root node=5 => 1 + max(0, 0)

BOTTOM UP CALCULATION

---> height of root node=8 => 1 + max(0, 0) #OUTPUT = 1 #DIAMETER = 0
---> height of root node=5 => 1 + max(0, 0) #OUTPUT = 1 #DIAMETER = 0

--> height of root node=6 => 1 + max(1, 0) #OUTPUT = 2 #DIAMETER = 1 + 0 = 1
--> height of root node=9 => 1 + max(1, 0) #OUTPUT = 2 #DIAMETER = 1 + 0 = 1

-> height of root node=7 => 1 + max(2,2) #OUTPUT = 3 #DIAMETER = 2 + 2 = 4

height of root node=4 => 1 + max(3, 0) #OUTPUT 4 ##DIAMETER = 3 + 0 = 3

MAX DIAMETER = 4

'''

    
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diameter = 0
        def dfs(root):

            if not root:
                return 0

            height_right = dfs(root.right) #  passing in the left child of the current node, which becomes the new root for the recursive call
            height_left = dfs(root.left) #  passing in the right child of the current node, which becomes the new root for the recursive call
            self.diameter = max(self.diameter, height_right + height_left)

            return 1 + max(height_left, height_right)

        dfs(root)
        return self.diameter
    



'''
Trees
EASY

4. Balanced Binary Tree:

Given a binary tree, determine if it is height-balanced
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one

# QUESTION

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:

Input: root = []
Output: true


# SOLUTION

recursive dfs:

calculating from bottom up to make the T O(N) =>
need the:
height: in terms of integer so we can calculate the difference 
difference of subtrees: output in form of boolean TRUE if diff between height is 0, 1, else FALSE  
    
'''     

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def dfs(root):
            if not root:
                return [True, 0] 
            right = dfs(root.right) 
            left = dfs(root.left)
            balanced = (left[0] and right[0] and abs(right[1] - left[1]) <= 1)

            return [balanced, 1 + max(left[1], right[1])]  #root[0,1] = balance: bool, height: int

        return dfs(root)[0] #root[0] = bool



'''
Trees
EASY

5. Same Tree


# QUESTION

Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:

Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:

Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:

Input: p = [1,2,1], q = [1,1,2]
Output: false

# SOLUTION

recursive dfs:
if theyre both empty trees: identical: True
if the tree is not empty AND the values are same: return True
Else False


'''


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left) #both structure and val OF ALL has to be same to return true
        else:
            return False


