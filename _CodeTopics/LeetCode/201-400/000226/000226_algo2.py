# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if not root:
            return None
        
        q = [root]
        while q:
            nextLevel, length = [], len(q)
            # 本来想着用下面这句每层倒过来循环，后来发现那下一层又不对了啊。然后仔细想想明白了：
            # nextLevel还是按翻转前的顺序往里append就行，只是每贴进去一个，就把左右子节点翻转好，
            # 下一层直接就是好的。
            # for i in range(length - 1, -1, -1):
            for node in q:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
                node.left, node.right = node.right, node.left
            q = nextLevel
        return root
        
"""
https://leetcode-cn.com/submissions/detail/108745695/

68 / 68 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 12.6 MB
"""
"""
执行用时：24 ms, 在所有 Python 提交中击败了40.86%的用户
内存消耗：12.6 MB, 在所有 Python 提交中击败了13.45%的用户
"""
