"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        if not root:
            return []
        
        stk = deque([root])
        res = []
        while stk:
            currLevel = []
            for i in range(len(stk)):
                node = stk.popleft()
                currLevel.append(node.val)
                stk.extend(node.children)
            res.append(currLevel)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/296778548/

执行用时：
56 ms
, 在所有 Python3 提交中击败了
65.17%
的用户
内存消耗：
16.9 MB
, 在所有 Python3 提交中击败了
43.79%
的用户
通过测试用例：
38 / 38
"""
