# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        def is_leaf(node):
            return False if node.left or node.right else True
        
        def dfs_inorder_2(node, lis):
            if not node:
                return
            if is_leaf(node):
                lis.append(node.val)
            else:
                dfs_inorder_2(node.left, lis)
                dfs_inorder_2(node.right, lis)
        
        # 试试每次都把类内变量重置，看能不能解决——官方说能，但是官方的帖子下面有人说即使这样也不能。。。
        # `为什么某些测试用例下，执行代码返回结果正确，但提交解答却出错了` https://support.leetcode-cn.com/hc/kb/article/1194344/
        # 后来试了下根本不行，所以换方法重写了，只能是不用全局变量或类内类似list之类的变量。

        leaves1, leaves2 = [], []
        dfs_inorder_2(root1, leaves1)
        dfs_inorder_2(root2, leaves2)
        return leaves1 == leaves2
        
"""
https://leetcode-cn.com/submissions/detail/175930294/

40 / 40 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13 MB

执行用时：24 ms, 在所有 Python 提交中击败了47.92%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了90.62%的用户
"""
