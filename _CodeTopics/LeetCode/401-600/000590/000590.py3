"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        res = []
        def postorder_dfs_n_ary_tree(node: Node = None) -> None:
            if not node:
                return
            for child in node.children:
                postorder_dfs_n_ary_tree(child)
            res.append(node.val)
        
        postorder_dfs_n_ary_tree(root)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/281572173/

执行用时：56 ms, 在所有 Python3 提交中击败了39.29%的用户
内存消耗：17 MB, 在所有 Python3 提交中击败了21.03%的用户
通过测试用例：
38 / 38
"""
