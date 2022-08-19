# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        if not nums:
            return None
        elif len(nums) == 1:
            return TreeNode(nums[0])
        
        maxVal = max(nums)
        maxInd = nums.index(maxVal)
        node = TreeNode(maxVal)
        node.left = self.constructMaximumBinaryTree(nums[:maxInd])
        node.right = self.constructMaximumBinaryTree(nums[maxInd+1:])
        return node
        
"""
https://leetcode.cn/submissions/detail/352511703/

执行用时：
92 ms
, 在所有 Python3 提交中击败了
98.72%
的用户
内存消耗：
15.6 MB
, 在所有 Python3 提交中击败了
18.25%
的用户
通过测试用例：
107 / 107
"""
