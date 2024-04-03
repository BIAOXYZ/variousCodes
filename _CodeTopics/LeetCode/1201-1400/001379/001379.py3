# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        # 这题之所以是简单，主要是因为节点值都不相同。。。所以对原始树甚至都不需要遍历- -
        # 直接在克隆树上找 val 等于 target.val 的那个节点就行。
        # 当然，这题也可以解得更有通用性一点。

        def dfs_and_compare_value(node):
            if not node:
                return
            if node.val == target.val:
                return node
            left_return = dfs_and_compare_value(node.left)
            right_return = dfs_and_compare_value(node.right)
            return left_return if left_return is not None else right_return
        
        return dfs_and_compare_value(cloned)
        
"""
https://leetcode.cn/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/submissions/519951224?envType=daily-question&envId=2024-04-03

通过
零知识证明
提交于 2024.04.04 00:37

执行用时分布
322
ms
击败
33.54%
使用 Python3 的用户
消耗内存分布
24.10
MB
击败
96.84%
使用 Python3 的用户
"""
