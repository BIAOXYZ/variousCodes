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
        paths[0] = ['U'] * len(paths[0])
        return ''.join(paths[0]) + ''.join(paths[1])
    
"""
https://leetcode-cn.com/submissions/detail/245390403/

86 / 332 个通过测试用例
状态：解答错误

输入：
[1,null,10,12,13,4,6,null,15,null,null,5,11,null,2,14,7,null,8,null,null,null,9,3]
6
15
输出：
"UUURRR"
预期：
"UURR"
"""
