# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:

        dic = {}
        def dfs_and_count_node_number(node):
            dic[node.val] = 1
            if node.left:
                dic[node.val] += dfs_and_count_node_number(node.left)
            if node.right:
                dic[node.val] += dfs_and_count_node_number(node.right)
            return dic[node.val]
        
        dfs_and_count_node_number(root)
        if root.val == x:
            return True if any(dic[node.val] > (n-1)//2 for node in [root.left, root.right]) else False
        else:
            return True if dic[x] <= (n-1)//2 else False
        
"""
https://leetcode.cn/submissions/detail/399091313/

64 / 65 个通过测试用例
状态：解答错误

输入：
[6,3,null,7,4,null,null,null,2,null,1,null,5]
7
3
输出：
false
预期结果：
true
"""
