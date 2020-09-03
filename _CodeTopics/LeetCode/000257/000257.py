# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    currPath = ''
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        if not root:
            return []
        
        res = []
        # Python2 没有nonlocal真难受。。。只能定义成类成员变量，然后加self来用。但是list就可以，忘了是为啥了。
        # currPath = ''

        def dfs_and_record_path(node):
            if not node.left and not node.right:
                res.append(self.currPath + str(node.val))
                return
            newpart = str(node.val) + '->'
            if node.left:
                self.currPath = self.currPath + newpart
                dfs_and_record_path(node.left)
                self.currPath = self.currPath[:-len(newpart)]
            if node.right:
                self.currPath = self.currPath + newpart
                dfs_and_record_path(node.right)
                self.currPath = self.currPath[:-len(newpart)]
            return
        
        dfs_and_record_path(root)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/104552592/

209 / 209 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 12.8 MB
"""
"""
执行用时：32 ms, 在所有 Python 提交中击败了10.69%的用户
内存消耗：12.8 MB, 在所有 Python 提交中击败了45.71%的用户
"""
