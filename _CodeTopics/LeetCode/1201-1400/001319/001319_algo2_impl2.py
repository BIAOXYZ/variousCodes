from collections import defaultdict
class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """

        length = len(connections)
        if length < n - 1:
            return -1

        def dfs(i):
            for ind in dic[i]:
                if ind not in visited:
                    visited.add(ind)
                    dfs(ind)

        # 构造一个该图对应的数据结构，这里用字典了。

        # 但是有的点 i 根本没有一条边连接，表现就是在字典 dic 里就没有 i 这个key。为了解决这个问题，之前的做法是在dfs()函数
        # 里面进行处理：如果没有这个key，直接return就好，因为没必要继续查找下去了。
        # 如前一个实现（`001319_algo2_impl.py`）中所述：这次用 `collections` 里的 `defaultdict`类的实现。
        dic = defaultdict(set)
        for edge in connections:
            a, b = edge[0], edge[1]
            dic[a].add(b)
            dic[b].add(a)
        
        visited, numOfConnectedComponent = set([]), 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                numOfConnectedComponent += 1
                dfs(i)
        return numOfConnectedComponent - 1
        
"""
https://leetcode-cn.com/submissions/detail/140603120/

36 / 36 个通过测试用例
状态：通过
执行用时: 160 ms
内存消耗: 42.1 MB

执行用时：160 ms, 在所有 Python 提交中击败了61.54%的用户
内存消耗：42.1 MB, 在所有 Python 提交中击败了15.38%的用户
"""
