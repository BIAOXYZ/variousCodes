# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        
        res = []
        def dfs_preorder(node):
            if not node:
                return
            res.append(str(node.val))
            dfs_preorder(node.left)
            dfs_preorder(node.right)
        dfs_preorder(root)
        return '' if not res else '|'.join(res)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """

        def dfs_restore(lis):
            father = TreeNode(lis[0])
            length = len(lis)
            if length == 1:
                return father
            leftStart = None
            if lis[1] < lis[0]:
                leftStart = 1
            rightStart = None
            for i in range(1, length):
                if lis[i] > lis[0]:
                    rightStart = i
                    break
            if leftStart and rightStart:
                father.left = dfs_restore(lis[1:i])
                father.right = dfs_restore(lis[i:])
            elif leftStart:
                father.left = dfs_restore(lis[1:])
            elif rightStart:
                father.right = dfs_restore(lis[1:])
            return father
        
        if not data:
            return None
        data = list(map(int, data.split('|')))
        return dfs_restore(data)


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans

"""
https://leetcode.cn/submissions/detail/312069782/

执行用时：
92 ms
, 在所有 Python3 提交中击败了
40.18%
的用户
内存消耗：
19.3 MB
, 在所有 Python3 提交中击败了
56.47%
的用户
通过测试用例：
62 / 62
"""
