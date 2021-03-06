class Solution(object):
    def countPairs(self, n, edges, queries):
        """
        :type n: int
        :type edges: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        
        dic = {}
        for edge in edges:
            small, large = min(edge), max(edge)
            for i in range(1, small):
                key = str(i) + str(small)
                dic[key] = dic.setdefault(key, 0) + 1
            for i in range(small+1, n+1):
                key = str(small) + str(i)
                dic[key] = dic.setdefault(key, 0) + 1
            for j in range(1, small) + range(small+1, large):
                key = str(j) + str(large)
                dic[key] = dic.setdefault(key, 0) + 1
            for j in range(large+1, n+1):
                key = str(large) + str(j)
                dic[key] = dic.setdefault(key, 0) + 1
            
        lis = dic.values()
        lis.sort()
        length = len(lis)
        
        res = []
        for query in queries:
            i = bisect.bisect_right(lis, query)
            res.append(length - i)
        return res
    
"""
https://leetcode-cn.com/submissions/detail/151933420/

47 / 63 个通过测试用例
状态：超出时间限制
"""
