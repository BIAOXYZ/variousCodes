# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:

        ctr = Counter()
        def dfs(node):
            if not node:
                return 0
            total = node.val + dfs(node.left) + dfs(node.right)
            ctr[total] += 1
            return total
        
        dfs(root)
        maxFreq = max(ctr.values())
        return [summ for summ, freq in ctr.items() if freq == maxFreq]
        
"""
https://leetcode.cn/submissions/detail/326729614/

执行用时：
52 ms
, 在所有 Python3 提交中击败了
64.10%
的用户
内存消耗：
18.5 MB
, 在所有 Python3 提交中击败了
75.64%
的用户
通过测试用例：
58 / 58
"""
