# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs_get_depth_and_father(node):
            currDepth = dic_node_depth[node]
            nextDepth = currDepth + 1
            children = [node.left, node.right]
            for child in children:
                if child:
                    dic_node_depth[child], dic_node_father[child] = nextDepth, node
                    if nextDepth not in dic_depth_nodes:
                        dic_depth_nodes[nextDepth] = [child]
                    else:
                        dic_depth_nodes[nextDepth].append(child)
                    dfs_get_depth_and_father(child)

        dic_node_depth = {root:0}
        dic_node_father = {root: None}
        dic_depth_nodes = {0:[root]}
        dfs_get_depth_and_father(root)
        
        max_depth_child = dic_depth_nodes[max(dic_depth_nodes.keys())]
        while len(max_depth_child) > 1:
            se = set()
            for child in max_depth_child:
                father = dic_node_father[child]
                se.add(father)
            max_depth_child = se
        return list(max_depth_child)[0]
        
"""
https://leetcode.cn/problems/lowest-common-ancestor-of-deepest-leaves/submissions/463680584/?envType=daily-question&envId=2023-09-06

时间
详情
52ms
击败 81.82%使用 Python3 的用户
内存
详情
16.24MB
击败 47.27%使用 Python3 的用户
"""
