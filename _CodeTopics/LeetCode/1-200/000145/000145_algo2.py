# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        # 这个是和 000144_algo2.py 完全对称的代码。结果集每次往左边贴；临时栈里
        ## 保存的都是curr的左孩子；每次先沿着右孩子往下DFS遍历。
        ## 注意：只是结果集用deque，存树的节点的临时栈还是用list。
        # 但是这种写法还是有点hack，回头再找个别的写法。反正需要达到三种非递归遍历
        ## 方式的形式基本类似，只改动少许代码即可。
        res = deque([])
        curr = root
        leftChildrenStack = []

        while curr:
            res.appendleft(curr.val)
            if curr.left:
                leftChildrenStack.append(curr.left)
            if curr.right:
                curr = curr.right
            elif leftChildrenStack:
                curr = leftChildrenStack.pop()
            else:
                break
        return res
        
"""
https://leetcode-cn.com/submissions/detail/118853272/

68 / 68 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13.2 MB

执行用时：24 ms, 在所有 Python 提交中击败了31.23%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了5.05%的用户
"""
