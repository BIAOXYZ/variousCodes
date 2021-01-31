class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        
        def int_to_sum(n):
            res = 0
            while n > 0:
                res += n % 10
                n /= 10
            return res
        
        dic = {}
        for i in range(lowLimit, highLimit+1):
            num = int_to_sum(i)
            if dic.has_key(num):
                dic[num] += 1
            else:
                dic[num] = 1
        return max(dic.values())
    
"""
https://leetcode-cn.com/submissions/detail/142468725/

97 / 97 个通过测试用例
状态：通过
执行用时: 440 ms
内存消耗: 15.7 MB
"""
