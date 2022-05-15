# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:

        if not root or not p:
            return None

        vals, nodes = [], []
        def dfs_inorder(node):
            if not node:
                return
            dfs_inorder(node.left)
            vals.append(node.val)
            nodes.append(node)
            dfs_inorder(node.right)
        
        dfs_inorder(root)
        ind = bisect.bisect_right(vals, p.val)
        return None if ind == len(vals) else nodes[ind]
        
"""
https://leetcode.cn/submissions/detail/314011070/

执行用时：
68 ms
, 在所有 Python3 提交中击败了
90.73%
的用户
内存消耗：
19.1 MB
, 在所有 Python3 提交中击败了
33.14%
的用户
通过测试用例：
24 / 24
"""
