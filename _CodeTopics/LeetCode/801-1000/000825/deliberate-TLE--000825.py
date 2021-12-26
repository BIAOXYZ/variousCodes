class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """

        # 这个应该会超时。。。

        def satisfy_conditions(age1, age2):
            return age2 <= 0.5 * age1 + 7 or age2 > age1 or (age2 > 100 and age1 < 100)
        
        length = len(ages)
        ages.sort()
        res = 0
        for i in range(length-1):
            for j in range(i+1, length):
                if not satisfy_conditions(ages[j], ages[i]):
                    if ages[i] != ages[j]:
                        res += 1
                    else:
                        res += 2
        return res
        
"""
https://leetcode-cn.com/submissions/detail/252320557/

73 / 88 个通过测试用例
状态：超出时间限制
"""
