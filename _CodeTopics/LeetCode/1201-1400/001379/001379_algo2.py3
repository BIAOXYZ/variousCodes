# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        # 更通用一点的解法：先遍历原始树，得到一个 LR 序列；然后利用这个序列去克隆树找目标节点

        def dfs_get_LR_path(node, target, curr_path):
            if node is target:
                nonlocal path_to_target
                path_to_target = curr_path[:]
                return
            if node.left:
                curr_path.append("L")
                dfs_get_LR_path(node.left, target, curr_path)
                curr_path.pop()
            if node.right:
                curr_path.append("R")
                dfs_get_LR_path(node.right, target, curr_path)
                curr_path.pop()
        
        path_to_target = None
        dfs_get_LR_path(original, target, [])
        
        def dfs_according_to_path(node, path, pos):
            if pos == len(path):
                return node
            direction = path[pos]
            if direction == "L":
                return dfs_according_to_path(node.left, path, pos+1)
            else:
                return dfs_according_to_path(node.right, path, pos+1)
        
        return dfs_according_to_path(cloned, path_to_target, 0)
        
"""
https://leetcode.cn/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/submissions/519954548?envType=daily-question&envId=2024-04-03

通过
提交于 2024.04.04 01:15

执行用时分布
329
ms
击败
15.29%
使用 Python3 的用户
消耗内存分布
24.12
MB
击败
89.90%
使用 Python3 的用户
"""
