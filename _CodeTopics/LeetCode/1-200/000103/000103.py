# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []
        
        stk = [root]
        res = [[root.val]]
        # flag等于1时从左到右，等于-1时从右到左。
        flag = -1

        while stk:
            nextLevel, nextLevelVal = [], []
            for node in stk:
                if node.left:
                    nextLevel.append(node.left)
                    nextLevelVal.append(node.left.val)
                if node.right:
                    nextLevel.append(node.right)
                    nextLevelVal.append(node.right.val)
            stk = nextLevel
            if nextLevelVal:
                if flag == 1:
                    res.append(nextLevelVal[:])
                else:
                    res.append(nextLevelVal[::-1])
                flag = -flag
        return res
        
"""
https://leetcode-cn.com/submissions/detail/132757115/

33 / 33 个通过测试用例
状态：通过
执行用时: 8 ms
内存消耗: 13.4 MB

执行用时：8 ms, 在所有 Python 提交中击败了99.40%的用户
内存消耗：13.4 MB, 在所有 Python 提交中击败了14.17%的用户
"""
