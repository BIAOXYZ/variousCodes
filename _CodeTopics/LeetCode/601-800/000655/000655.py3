# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:

        def get_depth(node, depth):
            if not node:
                return depth-1
            return max(get_depth(node.left, depth+1), get_depth(node.right, depth+1))
        depth = get_depth(root, 0)
        m, n = depth + 1, 2**(depth+1)-1
        res = [["" for _ in range(n)] for _ in range(m)]

        def put_value(node, r, c):
            res[r][c] = str(node.val)
            if node.left:
                put_value(node.left, r+1, c - 2**(depth-r-1))
            if node.right:
                put_value(node.right, r+1, c + 2**(depth-r-1))
        put_value(root, 0, 2**depth-1)
        return res
        
"""
https://leetcode.cn/submissions/detail/353687098/

执行用时：
36 ms
, 在所有 Python3 提交中击败了
74.00%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
26.67%
的用户
通过测试用例：
73 / 73
"""
