# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        res = []
        if root is None:
            return res
        
        q = []
        q.append(root)

        while q != []:
            tmpnodelist = []
            curr_resval = []
            for elem in q:
                curr_resval.append(elem.val)
                if elem.left is not None:
                    tmpnodelist.append(elem.left)
                if elem.right is not None:
                    tmpnodelist.append(elem.right)
            q = tmpnodelist
            res.append(curr_resval)
        return res
        
"""
# https://leetcode-cn.com/submissions/detail/77126633/

34 / 34 个通过测试用例
状态：通过
执行用时：16 ms
内存消耗：13.2 MB
"""
