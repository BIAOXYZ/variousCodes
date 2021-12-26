class Solution(object):
    def getDistances(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
        dic = {}
        for i, num in enumerate(arr):
            if dic.has_key(num):
                dic[num].append(i)
            else:
                dic[num] = [i]
        
        intervals = [-1] * len(arr)
        visited = set()
        for i, num in enumerate(arr):
            if num in visited:
                continue
            visited.add(num)
            n = len(dic[num])
            mtx = [[0 for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    mtx[i][j] = abs(dic[num][i] - dic[num][j])
            vals = [sum(mtx[i]) for i in range(n)]
            for i in range(n):
                pos = dic[num][i]
                intervals[pos] = vals[i]
        return intervals
    
"""
https://leetcode-cn.com/submissions/detail/252108725/

56 / 61 个通过测试用例
状态：超出时间限制

最后执行的输入：
Hidden for this testcase during contest.
标准输出：
Hidden for this testcase during contest.
"""
