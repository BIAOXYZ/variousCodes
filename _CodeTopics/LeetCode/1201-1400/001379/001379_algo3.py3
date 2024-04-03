# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        # 更通用一点的解法2：两棵树一起遍历。

        if original is target:
            return cloned
        if not original:  # 此时 cloned 肯定也是 None，但是就不再额外判断了。
            return
        cloned_left_res = cloned_right_res = None
        if original.left:
            cloned_left_res = self.getTargetCopy(original.left, cloned.left, target)
        if original.right:
            cloned_right_res = self.getTargetCopy(original.right, cloned.right, target)
        return cloned_left_res if cloned_left_res is not None else cloned_right_res
        
"""
https://leetcode.cn/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/submissions/519960218?envType=daily-question&envId=2024-04-03

通过
提交于 2024.04.04 03:37

执行用时分布
320
ms
击败
25.65%
使用 Python3 的用户
消耗内存分布
24.25
MB
击败
30.57%
使用 Python3 的用户
"""
