# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        n = len(preorder)
        # lp，rp 分别表示当前 preorder 子数组在整个数组里的左右边界；
        # li，ri 类似，不过是对应 inorder 数组的。
        lp, rp, li, ri = 0, n-1, 0, n-1

        def build_from_indices(lp, rp, li, ri):
            if lp > rp:
                return None
            rootVal = preorder[lp]
            root = TreeNode(rootVal)
            if lp == rp:
                return root
            
            ind = inorder.index(rootVal)
            # 同上一个提交，lenRight 可以不用
            lenLeft, lenRight = ind - li, ri - ind
            liNextLeft, riNextLeft = li, ind
            liNextRight, riNextRight = ind+1, ri
            lpNextLeft, rpNextLeft = lp+1, lp+lenLeft
            lpNextRight, rpNextRight = lp+lenLeft+1, rp
            root.left = build_from_indices(lpNextLeft, rpNextLeft, liNextLeft, riNextLeft)
            root.right = build_from_indices(lpNextRight, rpNextRight, liNextRight, riNextRight)
            return root
        
        return build_from_indices(0, n-1, 0, n-1)
        
"""
https://leetcode.cn/submissions/detail/323653087/

执行用时：
68 ms
, 在所有 Python3 提交中击败了
72.54%
的用户
内存消耗：
19.5 MB
, 在所有 Python3 提交中击败了
67.43%
的用户
通过测试用例：
203 / 203
"""
