# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def is_empty_node(node):
            return not node
        def is_leaf(node):
            return node and not node.left and not node.right
        
        def dfs(node):
            if is_empty_node(node):
                return 0, 0
            elif is_leaf(node):
                return node.val, 0
            else:
                left_withnode, left_withoutnode = dfs(node.left)
                right_withnode, right_withoutnode = dfs(node.right)
                curr_withnode = node.val + left_withoutnode + right_withoutnode
                curr_withoutnode = max(left_withnode, left_withoutnode) + max(right_withnode, right_withoutnode)
                return curr_withnode, curr_withoutnode
        return max(dfs(root))
        
"""
https://leetcode.cn/problems/house-robber-iii/submissions/467204721/?envType=daily-question&envId=2023-09-18

时间
详情
52ms
击败 85.66%使用 Python3 的用户
内存
详情
18.07MB
击败 63.16%使用 Python3 的用户
"""
