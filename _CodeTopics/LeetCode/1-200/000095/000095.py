# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        def generateTreesFromList(l):
            if not l:
                return [None]

            res = []
            start, end = l[0], l[-1]            
            for i in range(start, end+1):
                leftlist = [j for j in range(start, i)]
                leftsubtree = generateTreesFromList(leftlist)
                rightlist = [k for k in range(i+1, end+1)]
                rightsubtree = generateTreesFromList(rightlist)

                for ltree in leftsubtree:
                    for rtree in rightsubtree:
                        root = TreeNode(i)
                        root.left = ltree
                        root.right = rtree
                        res.append(root)
            return res

        if n == 0:
            return []
        l = [i for i in range(1,n+1)]
        return generateTreesFromList(l)
        
"""
https://leetcode-cn.com/submissions/detail/90142382/

9 / 9 个通过测试用例
状态：通过
执行用时：52 ms
内存消耗：15.8 MB
"""
"""
执行用时：52 ms, 在所有 Python 提交中击败了35.39%的用户
内存消耗：15.8 MB, 在所有 Python 提交中击败了33.33%的用户
"""
