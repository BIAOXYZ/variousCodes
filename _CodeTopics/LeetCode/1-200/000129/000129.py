# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def is_leaf(node):
            return False if node.left or node.right else True
        def backtrack_dfs(node, currNum):
            currNum.append(node.val)
            if is_leaf(node):
                tmpsum, multiple = 0, 0
                for i in range(len(currNum)-1,-1,-1):
                    tmpsum += currNum[i] * (10**multiple)
                    multiple += 1
                ##print tmpsum
                res.append(tmpsum)
                currNum.pop()
                return
            if node.left:
                backtrack_dfs(node.left, currNum)
            if node.right:
                backtrack_dfs(node.right, currNum)
            currNum.pop()

        if not root:
            return 0
        # currNum, res = [], 0
        # 如果用上面那句，还是面临着res是个普通变量，而不是类似list等可以直接用的。
        currNum, res = [], []
        backtrack_dfs(root, currNum)
        return sum(res)
        
"""
https://leetcode-cn.com/submissions/detail/119382696/

110 / 110 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.2 MB

执行用时：20 ms, 在所有 Python 提交中击败了79.87%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了6.18%的用户
"""
