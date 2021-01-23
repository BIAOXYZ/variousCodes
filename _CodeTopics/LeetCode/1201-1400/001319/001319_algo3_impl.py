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
                        """
                        # 觉得下面这个if判断可以省略，直接往stk里append也没问题，因为反正还有是否在visited里那个if来判断。
                        if elem not in visited and elem not in stk:
                            stk.append(elem)
                        """
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
https://leetcode-cn.com/submissions/detail/140605903/

36 / 36 个通过测试用例
状态：通过
执行用时: 300 ms
内存消耗: 40.1 MB

执行用时：300 ms, 在所有 Python 提交中击败了46.15%的用户
内存消耗：40.1 MB, 在所有 Python 提交中击败了15.38%的用户
"""
