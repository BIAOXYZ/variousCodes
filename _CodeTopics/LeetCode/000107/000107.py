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

        q = [[root]]
        res = [[root.val]]
        while q[0]:
            nextLevel = []
            for currNode in q[0]:
                if currNode.left:
                    nextLevel.append(currNode.left)
                if currNode.right:
                    nextLevel.append(currNode.right)
            q.pop()
            if nextLevel:
                nextLevelVals = []
                for node in nextLevel:
                    nextLevelVals.append(node.val)
                res.append(nextLevelVals)
                q.append(nextLevel)
            else:
                return reverseList(res)
                
"""
https://leetcode-cn.com/submissions/detail/105361513/

34 / 34 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 13.2 MB
"""
"""
执行用时：28 ms, 在所有 Python 提交中击败了29.80%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了52.43%的用户
"""
