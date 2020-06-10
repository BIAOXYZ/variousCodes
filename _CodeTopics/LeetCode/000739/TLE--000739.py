class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """

        length = len(T)
        res = [0] * length

        for i in range(length):
            for j in range(i+1,length):
                if T[j] > T[i]:
                    res[i] = j - i
                    break
        return res
        
"""
https://leetcode-cn.com/submissions/detail/77974210/

28 / 37 个通过测试用例
状态：超出时间限制

最后执行的输入：
[47,34,47,34,47,47,34,34,47,47,34,47,47,47,47,34,47,34,34,47,34,34,34,47,34,47,34,47,34,47,34,34,34,34,34,47,34,34,...
"""
