"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        res = []
        def dfs_n_ary_tree(node):
            if not node:
                return
            res.append(node.val)
            for child in node.children:
                dfs_n_ary_tree(child)
        
        dfs_n_ary_tree(root)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/280427076/

执行用时：48 ms, 在所有 Python3 提交中击败了82.45%的用户
内存消耗：17 MB, 在所有 Python3 提交中击败了14.84%的用户
通过测试用例：
38 / 38
"""
