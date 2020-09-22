# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        def dfs_and_merge(node1, node2):
            node1.val += node2.val
            if node1.left and node2.left:
                dfs_and_merge(node1.left, node2.left)
            elif node1.left and not node2.left:
                pass
            elif not node1.left and node2.left:
                node1.left = node2.left
            else:
                pass
            
            if node1.right and node2.right:
                dfs_and_merge(node1.right, node2.right)
            elif node1.right and not node2.right:
                pass
            elif not node1.right and node2.right:
                node1.right = node2.right
            else:
                pass

        if not t1 and not t2:
            return None
        elif (not t1 and t2) or (t1 and not t2):
            return t1 if t1 else t2
        else:
            dfs_and_merge(t1, t2)
        return t1
        
"""
https://leetcode-cn.com/submissions/detail/110592940/

183 / 183 个通过测试用例
状态：通过
执行用时: 68 ms
内存消耗: 13.6 MB

执行用时：68 ms, 在所有 Python 提交中击败了92.27%的用户
内存消耗：13.6 MB, 在所有 Python 提交中击败了61.84%的用户
"""
