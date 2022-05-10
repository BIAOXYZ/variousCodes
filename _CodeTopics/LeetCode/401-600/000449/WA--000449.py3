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
        data = data.split('|')
        return dfs_restore(data)


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans

"""
https://leetcode.cn/submissions/detail/311915035/

11 / 62 个通过测试用例
状态：解答错误

输入：
[41,37,44,24,39,42,48,1,35,38,40,null,43,46,49,0,2,30,36,null,null,null,null,null,null,45,47,null,null,null,null,null,4,29,32,null,null,null,null,null,null,3,9,26,null,31,34,null,null,7,11,25,27,null,null,33,null,6,8,10,16,null,null,null,28,null,null,5,null,null,null,null,null,15,19,null,null,null,null,12,null,18,20,null,13,17,null,null,22,null,14,null,null,21,23]
输出：
[41,37,9,24,4,7,null,1,null,3,null,6,8,0,2,null,null,5,null,11,null,null,null,null,null,null,null,10,16,null,null,15,19,12,null,18,20,null,13,17,null,null,22,null,14,null,null,21,23,null,null,null,null,null,35,30,36,29,32,null,39,26,null,31,34,38,40,25,27,null,null,33,null,null,null,null,44,null,null,null,28,null,null,42,48,null,null,null,43,46,49,null,null,45,47]
预期结果：
[41,37,44,24,39,42,48,1,35,38,40,null,43,46,49,0,2,30,36,null,null,null,null,null,null,45,47,null,null,null,null,null,4,29,32,null,null,null,null,null,null,3,9,26,null,31,34,null,null,7,11,25,27,null,null,33,null,6,8,10,16,null,null,null,28,null,null,5,null,null,null,null,null,15,19,null,null,null,null,12,null,18,20,null,13,17,null,null,22,null,14,null,null,21,23]
"""
