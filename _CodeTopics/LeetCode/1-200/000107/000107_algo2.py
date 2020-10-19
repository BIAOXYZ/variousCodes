# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        """
        # 准备用python list自带的[::-1]语法糖，但是这个函数是没问题的，前面bfs的算法里都是用这个。
        def reverseList(l):
            length = len(l)
            for i in range(length/2):
                l[i], l[length-1-i] = l[length-1-i], l[i]
            return l
        """

        res = []
        if not root:
            return res

        def dfs(node, level):
            # 第0层，对应得res长度为1。所以对于某一个level值，len(res)的值应大于等于level + 1。
            if len(res) - 1 < level:
                res.append([])
            res[level].append(node.val)
            if not node.left and not node.right:
                return
            if node.left:
                dfs(node.left, level+1)
            if node.right:
                dfs(node.right, level+1)
        
        dfs(root, 0)
        return res[::-1]
        
"""
https://leetcode-cn.com/submissions/detail/105457101/

34 / 34 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13.5 MB
"""
"""
执行用时：24 ms, 在所有 Python 提交中击败了58.69%的用户
内存消耗：13.5 MB, 在所有 Python 提交中击败了9.06%的用户
"""
