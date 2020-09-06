# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        def reverseList(l):
            length = len(l)
            for i in range(length/2):
                l[i], l[length-1-i] = l[length-1-i], l[i]
            return l

        res = []
        if not root:
            return res

        q = [root]
        res = [[root.val]]
        while q:
            nextLevel = []
            for currNode in q:
                if currNode.left:
                    nextLevel.append(currNode.left)
                if currNode.right:
                    nextLevel.append(currNode.right)
            if nextLevel:
                nextLevelVals = []
                for node in nextLevel:
                    nextLevelVals.append(node.val)
                res.append(nextLevelVals)
                q = nextLevel
            else:
                return reverseList(res)
                
"""
https://leetcode-cn.com/submissions/detail/105362604/

34 / 34 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.3 MB
"""
"""
执行用时：20 ms, 在所有 Python 提交中击败了80.39%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了41.42%的用户
"""
