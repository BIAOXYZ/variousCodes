class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def has4Factors(num):
            list_factor = [1,num]
            i = 2
            # 这里必须是<=，否则6就不会被加进去（因为6的一半3不会去试了）
            while i <= num/2:
                # i是因子并且i没有在num的因子列表里出现过
                if num % i == 0 and list_factor.count(i) == 0:
                    list_factor.append(i)
                    if len(list_factor) > 4:
                        return [False]
                i+=1
            if len(list_factor) == 4:
                return [True, list_factor]
            else:
                return [False]
        
        sum = 0
        for num in nums:
            res = has4Factors(num)
            if res[0] is True:
                for factor in res[1]:
                    sum+=factor
        return sum

"""
提交结果：超出时间限制
最后执行的输入：[93307,17569,60314,75158,29520,68942,59392,79818,73491,92387,44424,64144,1872,52824,26050,79681,58141,50344,19302,...
"""
