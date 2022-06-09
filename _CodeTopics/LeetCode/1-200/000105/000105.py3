# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        # 其实下面这俩 or 连接在一起的非空的判断，用一个就够了。
        # 因为 preorder 和 inorder 每一回合的元素总数保持一致。
        if not preorder or not inorder:
            return None
        rootVal = preorder[0]
        root = TreeNode(rootVal)
        n = len(preorder)
        if n == 1:
            return root
        
        ind = inorder.index(rootVal)
        inorderLeft, inorderRight = inorder[:ind], inorder[ind+1:]
        # lenRight 其实可以不用计算
        lenLeft, lenRight = ind, n - 1 - ind
        preorderLeft, preorderRight = preorder[1:ind+1], preorder[ind+1:]
        
        left = self.buildTree(preorderLeft, inorderLeft)
        right = self.buildTree(preorderRight, inorderRight)
        root.left = left
        root.right = right
        return root
        
"""
https://leetcode.cn/submissions/detail/323652001/

执行用时：
152 ms
, 在所有 Python3 提交中击败了
41.39%
的用户
内存消耗：
88.4 MB
, 在所有 Python3 提交中击败了
5.09%
的用户
通过测试用例：
203 / 203
"""
