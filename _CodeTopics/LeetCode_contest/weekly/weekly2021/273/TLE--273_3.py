class Solution(object):
    def getDistances(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
        # 这个估计要超时。。。
        
        dic = {}
        for i, num in enumerate(arr):
            if dic.has_key(num):
                dic[num].append(i)
            else:
                dic[num] = [i]
        
        intervals = []
        for i, num in enumerate(arr):
            tmp = 0
            for pos in dic[num]:
                tmp += abs(i - pos)
            intervals.append(tmp)
        return intervals
    
"""
https://leetcode-cn.com/submissions/detail/252091751/

56 / 61 个通过测试用例
状态：超出时间限制

最后执行的输入：
Hidden for this testcase during contest.
标准输出：
Hidden for this testcase during contest.
"""
