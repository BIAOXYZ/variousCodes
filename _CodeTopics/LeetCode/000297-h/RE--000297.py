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
        if data is []:
            return []
        
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
https://leetcode-cn.com/submissions/detail/79549541/

1 / 48 个通过测试用例
状态：执行出错

执行出错信息：Line 52: TypeError: 'NoneType' object has no attribute '__getitem__'
最后执行的输入：[]
"""
"""
# print res 这句取消注释，然后执行代码是这样的：

输入
[1,2,3,null,null,4,5]
输出
[1,2,3,null,null,4,5]
预期结果
[1,2,3,null,null,4,5]
stdout
[[1], [2, 3], [None, None, 4, 5], [None, None, None, None]]
"""
