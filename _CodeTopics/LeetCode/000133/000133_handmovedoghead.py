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
        # 手动狗头题
        return copy.deepcopy(node)
        
"""
https://leetcode-cn.com/submissions/detail/97562263/

21 / 21 个通过测试用例
状态：通过
执行用时：48 ms
内存消耗：12.8 MB
"""
"""
执行用时：48 ms, 在所有 Python 提交中击败了72.18%的用户
内存消耗：12.8 MB, 在所有 Python 提交中击败了100.00%的用户
"""
