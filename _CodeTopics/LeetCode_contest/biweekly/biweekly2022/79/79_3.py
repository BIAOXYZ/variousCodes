class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        
        degree = [0] * n
        for n1, n2 in roads:
            degree[n1] += 1
            degree[n2] += 1
        ## print(degree)
        lis = [[i, degree[i]] for i in range(n)]
        lis.sort(key=lambda x : x[1], reverse=True)
        ## print(lis)
        return sum((n-i) * lis[i][1] for i in range(n))
    
"""
https://leetcode.cn/submissions/detail/319203867/

58 / 58 个通过测试用例
状态：通过
执行用时: 216 ms
内存消耗: 31.1 MB
"""
