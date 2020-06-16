# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return None
        
        res = [[root.val]]
        nodesCurrLevel = [root]
        while nodesCurrLevel != []:
            nodesNextLevel = []
            valueCurrLevel = []
            for node in nodesCurrLevel:
                if node.left is not None:
                    nodesNextLevel.append(node.left)
                    valueCurrLevel.append(node.left.val)
                else:
                    valueCurrLevel.append(None)
                if node.right is not None:
                    nodesNextLevel.append(node.right)
                    valueCurrLevel.append(node.right.val)
                else:
                    valueCurrLevel.append(None)
            nodesCurrLevel = nodesNextLevel
            res.append(valueCurrLevel)
        
        # 对于输入 [1,2,3,null,null,4,5]，结果为：
        # [[1], [2, 3], [None, None, 4, 5], [None, None, None, None]]
        # print res
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data is None:
            return None
        """
        # 对比前面的提交，所以这个if分支应该压根就没用。。。
        if data is []:
            return []
        """
        root = TreeNode(data[0][0])
        nodesPrevLevel = [root]
        # 最后一层肯定是一个全是None组成的list，可以直接忽略。
        for i in range(1,len(data)-1):
            nodesCurrLevel = []
            for j in range(len(data[i])):
                if j % 2 == 0:
                    pos = 'l'
                else:
                    pos = 'r'
                if data[i][j] is not None:
                    node = TreeNode(data[i][j])
                    if pos == 'l':
                        nodesPrevLevel[j/2].left = node
                    else:
                        nodesPrevLevel[j/2].right = node
                    nodesCurrLevel.append(node)
                else:
                    if pos == 'l':
                        nodesPrevLevel[j/2].left = None
                    else:
                        nodesPrevLevel[j/2].right = None
            nodesPrevLevel = nodesCurrLevel
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

"""
https://leetcode-cn.com/submissions/detail/79556200/

48 / 48 个通过测试用例
状态：通过
执行用时：100 ms
内存消耗：23 MB
"""
"""
执行结果：通过
显示详情
执行用时 :100 ms, 在所有 Python 提交中击败了95.90%的用户
内存消耗 :23 MB, 在所有 Python 提交中击败了100.00%的用户
"""
