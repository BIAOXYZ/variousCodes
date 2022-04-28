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
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        n = len(grid)
        if n == 1:
            return Node(grid[0][0], 1, None, None, None, None)
        if 0 < sum(sum(grid[i]) for i in range(n)) < n*n:
            topLeft = self.construct([[grid[i][j] for j in range(n//2)] for i in range(n//2)])
            topRight = self.construct([[grid[i][j] for j in range(n//2, n)] for i in range(n//2)])
            bottomLeft = self.construct([[grid[i][j] for j in range(n//2)] for i in range(n//2, n)])
            bottomRight = self.construct([[grid[i][j] for j in range(n//2, n)] for i in range(n//2, n)])
            curr = Node(grid[0][0], 0, topLeft, topRight, bottomLeft, bottomRight)
        else:
            curr = Node(grid[0][0], 1, None, None, None, None)
        return curr
        
"""
https://leetcode-cn.com/submissions/detail/306853721/

执行用时：
204 ms
, 在所有 Python3 提交中击败了
74.45%
的用户
内存消耗：
15.7 MB
, 在所有 Python3 提交中击败了
78.83%
的用户
通过测试用例：
22 / 22
"""
