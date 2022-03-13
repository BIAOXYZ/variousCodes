"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        if not root:
            return []
        res = []
        preorderStk = [root]
        
        while preorderStk:
            # 每次把当前节点 curr 弹出，把它的 val 放进 res；然后按照倒着来的顺序把它的每个孩子推进栈。
            # 比如假定 root 是 0，三个孩子从左到右分别是 1，2，3。那么 preorderStk 的变化过程是：
            ## [0] -- [3,2,1] -- [3,2] -- [3] -- []
            ## 层数更深的树也是类推一下就好。
            curr = preorderStk.pop()
            res.append(curr.val)
            for i in range(len(curr.children)-1, -1, -1):
                preorderStk.append(curr.children[i])
        return res
        
"""
https://leetcode-cn.com/submissions/detail/282292321/

执行用时：48 ms, 在所有 Python3 提交中击败了90.51%的用户
内存消耗：17 MB, 在所有 Python3 提交中击败了48.33%的用户
通过测试用例：
38 / 38
"""
