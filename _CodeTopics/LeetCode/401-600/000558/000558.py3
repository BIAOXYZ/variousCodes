"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        
        if not quadTree1.isLeaf and not quadTree2.isLeaf:
            topLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
            topRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
            bottomLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
            bottomRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
            if all(node.isLeaf and node.val == 1 for node in [topLeft, topRight, bottomLeft, bottomRight]):
                quadTree = Node(1, True, None, None, None, None)
            else:
                quadTree = Node(quadTree1.val, False, topLeft, topRight, bottomLeft, bottomRight)
        elif (quadTree1.isLeaf and quadTree1.val == 1) or (quadTree2.isLeaf and quadTree2.val == 1):
            quadTree = Node(1, True, None, None, None, None)
        elif quadTree1.isLeaf and quadTree1.val == 0:
            quadTree = copy.deepcopy(quadTree2)
        elif quadTree2.isLeaf and quadTree2.val == 0:
            quadTree = copy.deepcopy(quadTree1)
        return quadTree
        
"""
https://leetcode.cn/submissions/detail/338230635/

执行用时：
80 ms
, 在所有 Python3 提交中击败了
15.71%
的用户
内存消耗：
15.9 MB
, 在所有 Python3 提交中击败了
5.71%
的用户
通过测试用例：
61 / 61
"""
