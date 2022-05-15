# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:

        # 上一个写法（`WA--04.06_algo2.py3`）大的思路上有问题，参见那个错误用例就知道了。

        res = None
        curr = root
        while curr:
            if curr.val <= p.val:
                curr = curr.right
            elif curr.val > p.val:
                res = curr
                curr = curr.left
        return res
        
"""
https://leetcode.cn/submissions/detail/314033950/

执行用时：
76 ms
, 在所有 Python3 提交中击败了
64.83%
的用户
内存消耗：
19.1 MB
, 在所有 Python3 提交中击败了
20.04%
的用户
通过测试用例：
24 / 24
"""
