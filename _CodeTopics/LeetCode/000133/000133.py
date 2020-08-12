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

        visited = {}

        def dfs(node):
            if visited.has_key(node):
                return visited[node]
            nodecopy = Node(node.val, [])
            visited[node] = nodecopy
            for elem in node.neighbors:
                elemcopy = dfs(elem)
                nodecopy.neighbors.append(elemcopy)
            return nodecopy
        
        return dfs(node)

"""
https://leetcode-cn.com/submissions/detail/97507394/

21 / 21 个通过测试用例
状态：通过
执行用时：52 ms
内存消耗：13.2 MB
"""
"""
执行用时：52 ms, 在所有 Python 提交中击败了50.54%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了20.59%的用户
"""
