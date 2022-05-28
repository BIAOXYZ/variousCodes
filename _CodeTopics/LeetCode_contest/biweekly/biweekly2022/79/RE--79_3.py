class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        
        degree = defaultdict(int)
        for n1, n2 in roads:
            degree[n1] += 1
            degree[n2] += 1
        kv = [[k, v] for k, v in degree.items()]
        kv.sort(key=lambda x : x[1], reverse=True)
        return sum((n-i) * kv[i][1] for i in range(n))
    
"""
https://leetcode.cn/submissions/detail/319202540/

3 / 58 个通过测试用例
状态：执行出错

执行出错信息：
IndexError: list index out of range
    return sum((n-i) * kv[i][1] for i in range(n))
Line 10 in <genexpr> (Solution.py)
    return sum((n-i) * kv[i][1] for i in range(n))
Line 10 in maximumImportance (Solution.py)
    ret = Solution().maximumImportance(param_1, param_2)
Line 37 in _driver (Solution.py)
    _driver()
Line 48 in <module> (Solution.py)
最后执行的输入：
5
[[0,1]]
"""
