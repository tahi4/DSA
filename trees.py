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

1. recursive  DFS -Depth First Search recursive algorithm to search all the vertices of a tree data structure

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


 

'''

