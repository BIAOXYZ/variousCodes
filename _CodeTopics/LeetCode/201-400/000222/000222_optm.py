# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # BFS层序遍历，有优化：
        # 在遍历某一层的节点时，一旦发现某个node的左右孩子中至少有一个为空，就可以直接返回结果了。
        # 此外，这种实现不是每层开始求一下len(stk)再加上去，而且在遍历上一层的过程中直接算下一层的。

        if not root:
            return 0
        res = 1
        stk = [root]
        
        while stk:
            nextLevel = []
            for node in stk:
                if node.left:
                    nextLevel.append(node.left)
                    res += 1
                else:
                    return res
                if node.right:
                    nextLevel.append(node.right)
                    res += 1
                else:
                    return res
            stk = nextLevel[:]
        return res
        
"""
https://leetcode-cn.com/submissions/detail/125764828/

18 / 18 个通过测试用例
状态：通过
执行用时: 72 ms
内存消耗: 28.4 MB

执行用时：72 ms, 在所有 Python 提交中击败了82.06%的用户
内存消耗：28.4 MB, 在所有 Python 提交中击败了19.14%的用户
"""
