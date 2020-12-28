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
        """
        # 第一次这里写36结果用例9999时会提示: 
        
        提交结果：执行出错 
        执行错误信息：Line 21: IndexError: list index out of range
        最后执行的输入：9999
        """
        grouplist = [0] * 37
        for i in range(1,n+1):
            val = valueOfNumber(i)
            grouplist[val] += 1
        return grouplist.count(max(grouplist))
