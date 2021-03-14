class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        
        n = len(edges) + 1
        degree = [0] * (n+1)
        for edge in edges:
            degree[edge[0]] += 1
            degree[edge[1]] += 1
        print degree
        return degree.index(max(degree))
    
"""
https://leetcode-cn.com/submissions/detail/154897747/

60 / 60 个通过测试用例
状态：通过
执行用时: 244 ms
内存消耗: 33.7 MB
"""
