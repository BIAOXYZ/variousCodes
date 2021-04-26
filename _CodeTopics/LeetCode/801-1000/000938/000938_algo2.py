# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """

        # BFS实现（已经带了剪枝）

        res = 0
        stk = [root]
        while stk:
            curr = stk.pop(0)
            if curr.val < low:
                if curr.right:
                    stk.append(curr.right)
            elif curr.val > high:
                if curr.left:
                    stk.append(curr.left)
            else:
                res += curr.val
                if curr.left:
                    stk.append(curr.left)
                if curr.right:
                    stk.append(curr.right)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/172319886/

41 / 41 个通过测试用例
状态：通过
执行用时: 268 ms
内存消耗: 28.7 MB

执行用时：268 ms, 在所有 Python 提交中击败了53.60%的用户
内存消耗：28.7 MB, 在所有 Python 提交中击败了92.09%的用户
"""
