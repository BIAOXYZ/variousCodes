# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        dic = {}
        def dfs(node, currLen):
            if node.val not in dic:
                dic[node.val] = currLen
            else:
                dic[node.val] = max(dic[node.val], currLen)
            for child in [node.left, node.right]:
                if child:
                    if child.val == node.val:
                        dfs(child, currLen+1)
                    else:
                        dfs(child, 1)
        
        dfs(root, 0)
        return max(dic.values())
        
"""
https://leetcode.cn/submissions/detail/358269785/

25 / 71 个通过测试用例
状态：解答错误

输入：
[1,2]
输出：
1
预期结果：
0
"""
