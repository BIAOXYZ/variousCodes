class Solution(object):
    def goodDaysToRobBank(self, security, time):
        """
        :type security: List[int]
        :type time: int
        :rtype: List[int]
        """
        
        n = len(security)
        if n < 2 * time + 1:
            return []
        
        res = []
        center = time
        while center + time < n:
            leftflag = True
            for i in range(center-time, center):
                if security[i] < security[i+1]:
                    leftflag = False
                    break
            rightflag = True
            for j in range(center, center+time):
                if security[j] > security[j+1]:
                    rightflag = False
                    break
            if leftflag and rightflag:
                res.append(center)
            center += 1
        return res
    
"""
https://leetcode-cn.com/submissions/detail/247566297/

127 / 131 个通过测试用例
状态：超出时间限制

最后执行的输入：
Hidden for this testcase during contest.
标准输出：
Hidden for this testcase during contest.
"""
