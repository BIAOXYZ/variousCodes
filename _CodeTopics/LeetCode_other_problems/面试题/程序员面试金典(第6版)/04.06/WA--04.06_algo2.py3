# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:

        if not root or not p:
            return None

        # 容易看到，一旦找到了节点 p，一共其实就三种情况：
        # 1. p 的右孩子非空，此时结果就是 p 的右孩子。
        # 2. p 的右孩子为空，p 本身是其父亲的左孩子，此时结果就是 p 的父亲。
        # 3. p 的右孩子为空，p 本身是其父亲的右孩子，此时结果就是 p 的父亲的父亲。
        # 所以，只需要维护当前节点的父亲和祖父即可。
        def dfs_inorder(node, father, grandfather, direct):
            if not node:
                return
            leftRes = dfs_inorder(node.left, node, father, 'l')
            if leftRes:
                return leftRes
            if node.val == p.val:
                if node.right:
                    return node.right
                else:
                    if direct == 'l':
                        return father
                    elif direct == 'r':
                        return grandfather
            rightRes = dfs_inorder(node.right, node, father, 'r')
            return rightRes

        return dfs_inorder(root, None, None, '')
        
"""
https://leetcode.cn/submissions/detail/314028660/

19 / 24 个通过测试用例
状态：解答错误

输入：
[6,2,8,0,4,7,9,null,null,3,5]
2
输出：
4
预期结果：
3
"""
