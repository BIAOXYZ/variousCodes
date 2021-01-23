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
            if dic.setdefault(i, "notin") == "notin":
                return
            for ind in dic[i]:
                if ind not in visited:
                    visited.add(ind)
                    dfs(ind)

        # 构造一个该图对应的数据结构，这里用字典了。

        # 但是有的点 i 根本没有一条边连接，表现就是在字典 dic 里就没有 i 这个key。为了解决这个问题，之前的做法是在dfs()函数
        # 里面进行处理：如果没有这个key，直接return就好，因为没必要继续查找下去了。
        # 现在准备先用字典对象自带的方法 setdefault() 来处理缺失的默认值；后面再写一个用 `collections` 里的 `defaultdict`类的实现。
        dic = {}
        for edge in connections:
            a, b = edge[0], edge[1]
            if not dic.has_key(a):
                dic[a] = set([b])
            else:
                dic[a].add(b)
            if not dic.has_key(b):
                dic[b] = set([a])
            else:
                dic[b].add(a)
        
        visited, numOfConnectedComponent = set([]), 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                numOfConnectedComponent += 1
                dfs(i)
        return numOfConnectedComponent - 1
        
"""
https://leetcode-cn.com/submissions/detail/140599524/

36 / 36 个通过测试用例
状态：通过
执行用时: 152 ms
内存消耗: 42.2 MB

执行用时：152 ms, 在所有 Python 提交中击败了69.23%的用户
内存消耗：42.2 MB, 在所有 Python 提交中击败了15.38%的用户
"""
