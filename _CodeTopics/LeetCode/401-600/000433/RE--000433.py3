class Node(object):
    def __init__(self, s):
        self.val = s
        self.neighbors = []

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:

        def make_graph(lis):
            dic = {}
            for s in lis:
                dic[s] = Node(s)
            n = len(lis)
            for i in range(n-1):
                for j in range(i+1, n):
                    if is_neighbor(lis[i], lis[j]):
                        dic[lis[i]].neighbors.append(dic[lis[j]])
                        dic[lis[j]].neighbors.append(dic[lis[i]])
            return dic

        def is_neighbor(s1, s2):
            return sum(s1[i] != s2[i] for i in range(8)) == 1

        if start not in bank:
            bank.append(start)
        dic = make_graph(bank)

        # visited = set()
        # def dfs(node):
        #     if node in visited:
        #         return False
        #     if node.val == start:
        #         return True
        #     visited.add(node)
        #     res = False
        #     for nx in node.neighbors:
        #         res = res or dfs(nx)
        #     return res
        # return int(dfs(dic[end]))

        visited = set()
        q = deque([dic[end]])
        level = 0
        while q:
            n = len(q)
            for i in range(n):
                curr = q.popleft()
                if curr.val == start:
                    return level
                if curr not in visited:
                    visited.add(curr)
                else:
                    continue
                for child in curr.neighbors:
                    if child not in visited:
                        q.append(child)
            level += 1
        return -1
        
"""
https://leetcode-cn.com/submissions/detail/310201026/

3 / 14 个通过测试用例
状态：执行出错

执行出错信息：
KeyError: 'AACCGGTA'
    q = deque([dic[end]])
Line 42 in minMutation (Solution.py)
    ret = Solution().minMutation(param_1, param_2, param_3)
Line 90 in _driver (Solution.py)
    _driver()
Line 101 in <module> (Solution.py)
最后执行的输入：
"AACCGGTT"
"AACCGGTA"
[]
"""
