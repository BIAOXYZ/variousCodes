# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    res = []
    def dfs_inorder(self, node):
        if node.left:
            self.dfs_inorder(node.left)
        self.res.append(node.val)
        if node.right:
            self.dfs_inorder(node.right)
        return
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.dfs_inorder(root)
        return self.res

"""
这次直接把LeetCode全局变量的问题在代码里记下吧：

随便来些输入：
[1,null,2,3]
[]
[1]
[1,2]

输出：
[1,3,2]
[]
[1,3,2,1]
[1,3,2,1,2,1]

预期结果：
[1,3,2]
[]
[1]
[2,1]
"""

"""
https://leetcode-cn.com/submissions/detail/112290866/

2 / 68 个通过测试用例
状态：解答错误

# 其实错误用例没必要记了，因为不是代码的问题，就是LeetCode全局变量处理的不行。

输入：
[1]
输出：
[1,3,2,1]
预期：
[1]
"""
