class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """

        n = len(graph)
        res = []
        def backtrack(currNodes):
            if currNodes[-1] == n - 1:
                res.append(currNodes[:])
                return
            currNode = currNodes[-1]
            for nextNode in graph[currNode]:
                # 这种写法就不需要再处理回溯完的状态了。
                backtrack(currNodes + [nextNode])
        
        backtrack([0])
        return res
        
"""
https://leetcode-cn.com/submissions/detail/211255669/

30 / 30 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 16.1 MB

执行用时：20 ms, 在所有 Python 提交中击败了100.00%的用户
内存消耗：16.1 MB, 在所有 Python 提交中击败了70.15%的用户
"""
