# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # 这个写得也太丑陋（别扭）了。。。
        def max_node_num_in_path(node):
            if not node:
                return 0
            leftLongestPathNodeNum = max_node_num_in_path(node.left)
            rightLongestPathNodeNum = max_node_num_in_path(node.right)
            dic[node] = leftLongestPathNodeNum + rightLongestPathNodeNum
            return 1 + max(leftLongestPathNodeNum, rightLongestPathNodeNum)
        
        dic = {}
        if not root:
            return 0
        max_node_num_in_path(root)
        return max(dic.values())
        
"""
https://leetcode-cn.com/submissions/detail/121917537/

106 / 106 个通过测试用例
状态：通过
执行用时: 36 ms
内存消耗: 16.2 MB

执行用时：36 ms, 在所有 Python 提交中击败了51.02%的用户
内存消耗：16.2 MB, 在所有 Python 提交中击败了5.09%的用户
"""
