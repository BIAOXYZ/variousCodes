# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getDirections(self, root, startValue, destValue):
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str
        """
        
        paths = [[],[]]
        def dfs_with_path(node, path):
            if node.val == startValue:
                paths[0] = path
            if node.val == destValue:
                paths[1] = path
            if paths[0] != [] and paths[1] != []:
                return
            if node.left:
                dfs_with_path(node.left, path + ['L'])
            if node.right:
                dfs_with_path(node.right, path + ['R'])
        
        dfs_with_path(root, [])
        ##print paths
        
        commonPrefixLen = 0
        for i in range(min(len(paths[0]), len(paths[1]))):
            if paths[0][i] == paths[1][i]:
                commonPrefixLen += 1
            else:
                break
        paths[0] = paths[0][commonPrefixLen:]
        paths[1] = paths[1][commonPrefixLen:]
        
        paths[0] = ['U'] * len(paths[0])
        return ''.join(paths[0]) + ''.join(paths[1])
    
"""
https://leetcode-cn.com/submissions/detail/245394361/

287 / 332 个通过测试用例
状态：超出时间限制
"""
