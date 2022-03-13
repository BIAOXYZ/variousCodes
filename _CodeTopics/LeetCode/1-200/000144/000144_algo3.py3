# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # 后来受了多叉树前序遍历版本的影响，发现了新的更好记的写法。
        # https://leetcode-cn.com/submissions/detail/282292321/

        if not root:
            return []
        res = []
        preorderStk = [root]

        while preorderStk:
            curr = preorderStk.pop()
            res.append(curr.val)
            for node in [curr.right, curr.left]:
                if node:
                    preorderStk.append(node)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/282675938/

执行用时：36 ms, 在所有 Python3 提交中击败了56.10%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了95.60%的用户
通过测试用例：
69 / 69
"""
