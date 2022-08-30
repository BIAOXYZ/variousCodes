# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        # if val > root.val:
        #     node = TreeNode(val, root, None)
        # elif root.left and val > root.left.val:
        #     node = TreeNode(val, root.left, None)
        #     root.left = node
        # elif root.right and val > root.right.val:
        #     node = TreeNode(val, root.right, None)
        #     root.right = node
        # else:
        #     if root.left:
        #         node = self.insertIntoMaxTree(root.left)
        #     elif root.right:
        #         node = self.insertIntoMaxTree(root.right)
        #     else:
        #         node = TreeNode(val)
        #         root.left = node
        # return node

        if val > root.val:
            node = TreeNode(val, root, None)
            return node
        else:
            if not root.right:
                node = TreeNode(val)
                root.right = node
            else:
                node = self.insertIntoMaxTree(root.right, val)
                root.right = node
            return root
        
"""
https://leetcode.cn/submissions/detail/356904183/

执行用时：
28 ms
, 在所有 Python3 提交中击败了
98.31%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
46.61%
的用户
通过测试用例：
75 / 75
"""
