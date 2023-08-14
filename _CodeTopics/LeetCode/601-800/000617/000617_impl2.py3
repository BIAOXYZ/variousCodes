# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root1 and not root2:
            return None
        newnode = TreeNode()
        lchild1, rchild1 = None, None
        lchild2, rchild2 = None, None
        
        if root1:
            newnode.val += root1.val
            lchild1 = root1.left
            rchild1 = root1.right
        if root2:
            newnode.val += root2.val
            lchild2 = root2.left
            rchild2 = root2.right
        lchild = self.mergeTrees(lchild1, lchild2)
        rchild = self.mergeTrees(rchild1, rchild2)
        newnode.left = lchild
        newnode.right = rchild
        return newnode
        
"""
https://leetcode.cn/problems/merge-two-binary-trees/submissions/456367326/

时间
详情
84ms
击败 14.91%使用 Python3 的用户
内存
详情
17.10mb
击败 5.88%使用 Python3 的用户
"""
