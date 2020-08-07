# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        def double_dfs(p, q):
            if not p and not q:
                return True
            elif not p:
                return False 
            elif not q:
                return False
            else: 
                if p.val != q.val:
                    return False
                else:
                    return double_dfs(p.left, q.left) and double_dfs(p.right, q.right)
        
        return double_dfs(p, q)
                
"""
https://leetcode-cn.com/submissions/detail/95636379/

59 / 59 个通过测试用例
状态：通过
执行用时：24 ms
内存消耗：12.7 MB
"""
"""
执行用时：24 ms, 在所有 Python 提交中击败了41.93%的用户
内存消耗：12.7 MB, 在所有 Python 提交中击败了66.38%的用户
"""
