"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        if not root:
            return []
        res = deque([])
        postorderStk = [root]

        while postorderStk:
            curr = postorderStk.pop()
            for i in range(len(curr.children)):
                postorderStk.append(curr.children[i])
            res.appendleft(curr.val)
        return list(res)
        
"""
https://leetcode-cn.com/submissions/detail/282675664/

执行用时：52 ms, 在所有 Python3 提交中击败了74.37%的用户
内存消耗：17 MB, 在所有 Python3 提交中击败了20.89%的用户
通过测试用例：
38 / 38
"""
