class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:

        n = len(patience)
        dependenceDic = defaultdict(list)
        for u, v in edges:
            dependenceDic[u].append(v)
            dependenceDic[v].append(u)
        
        dic = {}
        depth = 0
        stk = deque([0])
        while stk:
            for _ in range(len(stk)):
                curr = stk.popleft()
                if curr in dic:
                    continue
                dic[curr] = depth
                for child in dependenceDic[curr]:
                    if child not in dic:
                        stk.append(child)
            depth += 1
        
        dis = list(dic.values())
        res = 0
        for i in range(1, n):
            tmp = 2*dis[i]
            if patience[i] < 2*dis[i]:
                quotient, remainder = 2*dis[i] // patience[i], 2*dis[i] % patience[i]
                if patience[i] > 1:
                    tmp = 4*dis[i] - remainder
                else:
                    tmp = 4*dis[i] - remainder - 1
            res = max(res, tmp)
        return res + 1
        
"""
https://leetcode-cn.com/submissions/detail/286373377/

15 / 50 个通过测试用例
状态：解答错误

输入：
[[5,7],[15,18],[12,6],[5,1],[11,17],[3,9],[6,11],[14,7],[19,13],[13,3],[4,12],[9,15],[2,10],[18,4],[5,14],[17,5],[16,2],[7,1],[0,16],[10,19],[1,8]]
[0,2,1,1,1,2,2,2,2,1,1,1,2,1,1,1,1,2,1,1]
输出：
68
预期结果：
67
"""
