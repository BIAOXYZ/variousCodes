class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        def valueOfNumber(x):
            val = 0
            while x >= 10:
                val += x % 10
                x = x / 10
            val += x
            return val
        
        # 1 <= n <= 10^4 的话，最大的和值也不过是9999的9*4=36
        grouplist = [None] * 36
        #maxsum = 1
        for i in range(1,n+1):
            val = valueOfNumber(i)
            if grouplist[val] is None:
                grouplist[val] = 1
            else:
                grouplist[val] += 1
            #if grouplist[val] > grouplist[maxsum]:
            #    maxsum = val
        #return grouplist[maxsum]
        return grouplist.count(max(grouplist))

"""
74 / 75 个通过测试用例
执行出错信息： Line 21: IndexError: list index out of range
最后执行的输入： 9999
"""
