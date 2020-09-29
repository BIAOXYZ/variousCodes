# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # 全局变量或类内变量有问题，只能是以参数形式传进函数里去了。
    # res = []
    def dfs_inorder(self, node, res):
        if node.left:
            self.dfs_inorder(node.left, res)
        res.append(node.val)
        if node.right:
            self.dfs_inorder(node.right, res)
        return
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return []
        self.dfs_inorder(root, res)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/112293796/

68 / 68 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 12.4 MB

执行用时：16 ms, 在所有 Python 提交中击败了88.29%的用户
内存消耗：12.4 MB, 在所有 Python 提交中击败了73.90%的用户
"""
