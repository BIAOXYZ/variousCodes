"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if not node:
            return node

        visited = []

        def dfs(node):
            if node in visited:
                return
            visited.append(node)
            nodecopy = Node(node.val, [])
            for elem in node.neighbors:
                elemcopy = dfs(elem)
                nodecopy.neighbors.append(elemcopy)
            return nodecopy
        
        return dfs(node)
        
"""
https://leetcode-cn.com/submissions/detail/97388878/

0 / 21 个通过测试用例
状态：执行出错

执行出错信息：
Line 100: AttributeError: 'NoneType' object has no attribute 'neighbors'
最后执行的输入：
[[2,4],[1,3],[2,4],[1,3]]
"""
