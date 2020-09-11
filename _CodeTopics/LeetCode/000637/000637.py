# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """

        q = [root]
        res = []

        while q:
            length = len(q)
            sum, nextLevel = 0, []
            for node in q:
                sum += node.val
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            # 不然第二层 (9 + 20) / 2 会取整，使得结果等于14，而不是14.5。
            res.append(sum * 1.0 / length)
            q = nextLevel
        return res
        
"""
https://leetcode-cn.com/submissions/detail/107150610/

65 / 65 个通过测试用例
状态：通过
执行用时: 40 ms
内存消耗: 17.5 MB
"""
"""
执行用时：40 ms, 在所有 Python 提交中击败了75.00%的用户
内存消耗：17.5 MB, 在所有 Python 提交中击败了21.59%的用户
"""
