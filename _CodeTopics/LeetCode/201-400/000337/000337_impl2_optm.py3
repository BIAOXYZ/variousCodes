# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        # https://leetcode.cn/problems/house-robber-iii/submissions/467204721 中 leaf 的情况完全不需要特殊处理。
        
        def is_empty_node(node):
            return not node
        
        def dfs(node):
            if is_empty_node(node):
                return 0, 0
            else:
                left_withnode, left_withoutnode = dfs(node.left)
                right_withnode, right_withoutnode = dfs(node.right)
                curr_withnode = node.val + left_withoutnode + right_withoutnode
                curr_withoutnode = max(left_withnode, left_withoutnode) + max(right_withnode, right_withoutnode)
                return curr_withnode, curr_withoutnode
        return max(dfs(root))
        
"""
https://leetcode.cn/problems/house-robber-iii/submissions/467204988/?envType=daily-question&envId=2023-09-18

时间
详情
48ms
击败 95.01%使用 Python3 的用户
内存
详情
18.11MB
击败 51.87%使用 Python3 的用户
"""
