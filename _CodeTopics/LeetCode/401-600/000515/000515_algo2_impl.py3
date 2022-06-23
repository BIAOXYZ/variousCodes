# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        dic = {}
        def dfs(node, level):
            if not node:
                return
            if level in dic:
                dic[level] = max(dic[level], node.val)
            else:
                dic[level] = node.val
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        
        dfs(root, 0)
        return list(dic.values())
        
"""
https://leetcode.cn/submissions/detail/328658041/

执行用时：
44 ms
, 在所有 Python3 提交中击败了
92.84%
的用户
内存消耗：
18 MB
, 在所有 Python3 提交中击败了
11.60%
的用户
通过测试用例：
78 / 78
"""
