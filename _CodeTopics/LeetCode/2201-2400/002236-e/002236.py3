# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:

        # 又一个比手动狗头题还简单的。。。
        return root.val == root.left.val + root.right.val
        
"""
https://leetcode.cn/problems/root-equals-sum-of-children/submissions/458032796/

时间
详情
40ms
击败 79.89%使用 Python3 的用户
内存
详情
15.57MB
击败 65.28%使用 Python3 的用户
"""
