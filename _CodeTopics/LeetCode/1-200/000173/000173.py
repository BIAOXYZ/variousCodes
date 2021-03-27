# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.val = []
        def dfs_postorder(node):
            if not node:
                return
            dfs_postorder(node.right)
            self.val.append(node.val)
            dfs_postorder(node.left)
        dfs_postorder(root)

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            return self.val.pop()

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.val else False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

"""
https://leetcode-cn.com/submissions/detail/160716908/

61 / 61 个通过测试用例
状态：通过
执行用时: 156 ms
内存消耗: 21 MB

执行用时：156 ms, 在所有 Python 提交中击败了84.09%的用户
内存消耗：21 MB, 在所有 Python 提交中击败了91.48%的用户
"""
