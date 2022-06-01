# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return root
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                return None
            if root.left and not root.right:
                return root.left
            elif not root.left and root.right:
                return root.right
            elif root.left and root.right:
                leftChild, rightChild = root.left, root.right
                smallest = rightChild
                while smallest.left:
                    smallest = smallest.left
                root.left = None
                root.right = None
                smallest.left = leftChild
                return rightChild
        return root
        
"""
https://leetcode.cn/submissions/detail/320806335/

执行用时：
56 ms
, 在所有 Python3 提交中击败了
89.61%
的用户
内存消耗：
19.7 MB
, 在所有 Python3 提交中击败了
5.02%
的用户
通过测试用例：
91 / 91
"""
