# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

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
https://leetcode.cn/submissions/detail/323651225/

2 / 203 个通过测试用例
状态：执行出错

执行出错信息：
IndexError: list index out of range
    rootVal = preorder[0]
Line 10 in buildTree (Solution.py)
    right = self.buildTree(preorderRight, inorderRight)
Line 23 in buildTree (Solution.py)
    ret = Solution().buildTree(param_1, param_2)
Line 53 in _driver (Solution.py)
    _driver()
Line 64 in <module> (Solution.py)
最后执行的输入：
[1,2]
[2,1]
"""
