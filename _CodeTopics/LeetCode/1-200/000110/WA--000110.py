# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    currHeight = 0
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # 思想：想了想算法就是计算出每个叶子节点的高度，然后只要有两个叶子节点的高度差大于1，
        # 就可以认为是不平衡的了。

        if not root:
            return True

        heightArr = []
        def dfs(node):
            if not node.left and not node.right:
                if self.currHeight not in heightArr:
                    heightArr.append(self.currHeight)
            elif node.left and not node.right:
                self.currHeight += 1
                dfs(node.left)
            elif not node.left and node.right:
                self.currHeight += 1
                dfs(node.right)
            else:
                self.currHeight += 1
                dfs(node.left)
                self.currHeight += 1
                dfs(node.right)
            self.currHeight -= 1
            return
        
        dfs(root)
        length = len(heightArr)
        if length > 2:
            return False
        elif length == 2:
            if abs(heightArr[0] - heightArr[1]) >= 2:
                return False
            return True
        elif length == 1:
            if heightArr[0] >= 2:
                return False
            return True
            
"""
https://leetcode-cn.com/submissions/detail/99106462/

166 / 227 个通过测试用例
状态：解答错误

输入：
[1,2,2,3,3,3,3,4,4,4,4,4,4,null,null,5,5]
输出：
false
预期：
true
"""
