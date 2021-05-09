# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # 这个就是LeetCode系统的bug：有些全局变量或者自定义的类内变量会有“纠缠”，比如这道题就是。。。
    # 把print打印取消注释执行下就知道了，各种ran一块。。。
    leaves1, leaves2 = [], []
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
        
        dfs_inorder_2(root1, self.leaves1)
        dfs_inorder_2(root2, self.leaves2)
        ##print self.leaves1, self.leaves2
        return self.leaves1 == self.leaves2
        
"""
https://leetcode-cn.com/submissions/detail/175928690/

23 / 40 个通过测试用例
状态：解答错误

最后执行的输入：
[1,2]
[2,2]
"""
"""
LeetCode系统这题已经Bug到只有“输入”，连“输出”和“预期”都没了都没了。。。一会截个图。
"""
