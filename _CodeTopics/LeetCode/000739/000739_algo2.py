class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """

        length = len(T)
        tempdic = {}
        res = [0 for i in range(length)]
        # 如果import sys的话，sys.maxint就是这个值，这里就是随便找个足够大的值。
        sysMaxInt = 9223372036854775807

        for i in range(length-1,-1,-1):
            # 不管有没有T[i]，都是这个语句。没有的话算新插入；有的话因为这个肯定比
            # 前面的某个i小，所以也更新成这个。
            tempdic[T[i]] = i
            minBiggerInd = sysMaxInt
            # 注意这里应为102，因为T[i]可能取100。
            for j in range(T[i] + 1, 102):
                minBiggerInd = min(minBiggerInd, tempdic.get(j, sysMaxInt))
            if minBiggerInd != sysMaxInt:
                res[i] = minBiggerInd - i
        return res
        
"""
https://leetcode-cn.com/submissions/detail/78219981/

37 / 37 个通过测试用例
状态：通过
执行用时：1828 ms
内存消耗：16 MB
"""
"""
吐槽：这执行时间。。。从没见过这么长的。是因为我随便取那个足够大的整数太大了么。。。一会python3一样的代码换个小点的那个整数试试。。。
"""
