# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        if not postorder:
            return None
        
        rootVal = postorder[-1]
        root = TreeNode(rootVal)
        if len(postorder) == 1:
            return root

        ind_inorder = inorder.index(rootVal)
        ind_postorder = postorder.index(rootVal)
        
        # 中序遍历的左子树和右子树很容易划分出来，就是 inorder[:ind_inorder] 和 inorder[ind_inorder+1:]。
        # 而对于后序遍历，其右子树没那么容易划分，会有一些陷阱。首先后序遍历的左子树和中序遍历左子树下标是一样的。
        # 然后右子树的话，其起始位置比中序遍历的右子树早一个位置，结束的位置晚一个位置。比如标准例子中的
        # inorder = [9,3,15,20,7] 和 postorder = [9,15,7,20,3]，看看[15,20,7]和[15,7,20]的位置就知道了。
        root.left = self.buildTree(inorder[:ind_inorder], postorder[:ind_inorder])
        root.right = self.buildTree(inorder[ind_inorder+1:], postorder[ind_inorder:ind_postorder])
        return root
        
"""
https://leetcode-cn.com/submissions/detail/111382454/

203 / 203 个通过测试用例
状态：通过
执行用时: 176 ms
内存消耗: 85.3 MB

执行用时：176 ms, 在所有 Python 提交中击败了18.73%的用户
内存消耗：85.3 MB, 在所有 Python 提交中击败了17.57%的用户
"""
