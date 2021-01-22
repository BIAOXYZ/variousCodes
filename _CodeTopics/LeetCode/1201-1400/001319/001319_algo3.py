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

        def bfs(i):
            if not dic.has_key(i):
                return
            stk = list(dic[i])
            while stk:
                ind = stk.pop(0)
                if ind not in visited:
                    visited.add(ind)
                    for elem in dic[ind]:
                        if elem not in visited and elem not in stk:
                            stk.append(elem)

        # 构造一个该图对应的数据结构，这里用字典了。
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
        
        visited, numOfConnectedComponent = set(), 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                numOfConnectedComponent += 1
                bfs(i)
        return numOfConnectedComponent - 1
        
"""
https://leetcode-cn.com/submissions/detail/140449034/

36 / 36 个通过测试用例
状态：通过
执行用时: 388 ms
内存消耗: 40.3 MB

执行用时：388 ms, 在所有 Python 提交中击败了38.46%的用户
内存消耗：40.3 MB, 在所有 Python 提交中击败了15.38%的用户
"""
