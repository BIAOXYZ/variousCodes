# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    res = []
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        # 这次是非子函数写法。

        if not root:
            return []
        
        if root.left:
            self.inorderTraversal(root.left)
        self.res.append(root.val)
        if root.right:
            self.inorderTraversal(root.right)
        return self.res
        
"""
https://leetcode-cn.com/submissions/detail/108020816/

2 / 68 个通过测试用例
状态：解答错误

输入：
[1]
输出：
[1,3,2,1]
预期：
[1]
"""
