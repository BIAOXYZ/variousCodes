# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # 先写个最plain的BFS层序遍历，无任何优化。

        if not root:
            return 0
        res = 0
        stk = [root]
        
        while stk:
            res += len(stk)
            nextLevel = []
            for node in stk:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            stk = nextLevel[:]
        return res
        
"""
https://leetcode-cn.com/submissions/detail/125764116/

18 / 18 个通过测试用例
状态：通过
执行用时: 72 ms
内存消耗: 28.4 MB

执行用时：72 ms, 在所有 Python 提交中击败了82.06%的用户
内存消耗：28.4 MB, 在所有 Python 提交中击败了17.29%的用户
"""
