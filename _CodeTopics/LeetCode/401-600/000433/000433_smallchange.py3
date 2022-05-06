class Node(object):
    def __init__(self, s):
        self.val = s
        self.neighbors = []

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:

        if end not in bank:
            return -1

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
                    # 其实上面有验证是否在 visited 的逻辑后，这里可以无脑 append 了。
                    # if child not in visited:
                    #     q.append(child)
                    q.append(child)
            level += 1
        return -1
        
"""
https://leetcode-cn.com/submissions/detail/310201259/

执行用时：
40 ms
, 在所有 Python3 提交中击败了
42.56%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
19.53%
的用户
通过测试用例：
14 / 14
"""
