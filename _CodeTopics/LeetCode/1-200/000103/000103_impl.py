# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []
        
        stk = [root]
        res = [[root.val]]
        # flag等于1时从左到右，等于-1时从右到左。
        flag = -1

        while stk:
            # 不使用额外的 nextLevel 数组，只是用当前栈不断pop(0)。就先不写用deque的版本了。
            nextLevelVal = []
            length = len(stk)
            for i in range(length):
                node = stk.pop(0)
                if node.left:
                    stk.append(node.left)
                    nextLevelVal.append(node.left.val)
                if node.right:
                    stk.append(node.right)
                    nextLevelVal.append(node.right.val)
            if nextLevelVal:
                if flag == 1:
                    res.append(nextLevelVal[:])
                else:
                    res.append(nextLevelVal[::-1])
                flag = -flag
        return res
        
"""
https://leetcode-cn.com/submissions/detail/132757224/

33 / 33 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13.3 MB

执行用时：24 ms, 在所有 Python 提交中击败了39.56%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了15.18%的用户
"""
