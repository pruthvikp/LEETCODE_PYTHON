'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:
The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
 
Follow up: Could you solve it both recursively and iteratively?
'''

# Brief explanation:
# The helper function is defined to recursively check if the left subtree of the current node is symmetric to the right subtree of another node.
# Inside helper, if both the left and right nodes are empty (i.e., None), return True.
# If either the left or right node is empty while the other is not, or if the values of the left and right nodes are not equal, return False.
# Recursively call helper with the left child of the left node and the right child of the right node, and vice versa, to check if the subtrees are symmetric.
# The isSymmetric function checks if the input tree is symmetric by calling helper with the root's left and right children.
# If the root is None, indicating an empty tree, return True.
# Otherwise, return the result of helper.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def helper(self,left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val==right.val:
            return self.helper(left.left,right.right) and self.helper(left.right,right.left)
        return False
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.helper(root.left,root.right)
        
