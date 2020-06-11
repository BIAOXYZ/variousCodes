
####################################################################################################
# 暂时没想明白为啥sysMaxInt不足够大（比如就取个1024）就会错。官方答案里是用10^9，我python2的代码取得很大，直接过了。
# 然后代码复制过来到python3里，第一次错了（输入太长不贴了，就记得我的程序里最后一堆0，但是正确答案并不是的，这点可以入手应该）
# 第二次换个够大的数（1024102410241024）就直接对了，其他代码一点没改。。。
# PS：python3果然效率更差，1024102410241024比python2版本里那个数（9223372036854775807）还小，但执行时间还是更长了。而且同样代码py3更慢不止一次了。。。
####################################################################################################

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:

        length = len(T)
        tempdic = {}
        res = [0 for i in range(length)]
        # 如果import sys的话，sys.maxint就是这个值，这里就是随便找个足够大的值。
        # 原来的是这个数：sysMaxInt = 9223372036854775807，结果时间巨长。
        # 这次换个小的，代码不变（换成python3提交了- -）试试看。
        sysMaxInt = 1024

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
https://leetcode-cn.com/submissions/detail/78222632/

25 / 37 个通过测试用例
状态：解答错误

输入：[44,35,67,81,94,70,48,33,61,36,95,99,83,83,90,68,39,41,53,58,49,38,67,45,58,86,39,96,78,37,58,90,37,69,99,100,74,84,71,33,95,...
输出：[2,1,1,1,6,5,2,1,2,1,1,24,2,1,13,10,1,1,1,3,2,1,3,1,1,2,1,7,3,1,1,3,1,1,1,0,1,3,2,1,31,1,3,1,1,11,9,8,2,1,1,4,1,1,1,1,3,2,1,12,...
预期：[2,1,1,1,6,5,2,1,2,1,1,24,2,1,13,10,1,1,1,3,2,1,3,1,1,2,1,7,3,1,1,3,1,1,1,0,1,3,2,1,31,1,3,1,1,11,9,8,2,1,1,4,1,1,1,1,3,2,1,12,...
"""

####################################################################################################

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:

        length = len(T)
        tempdic = {}
        res = [0 for i in range(length)]
        # 如果import sys的话，sys.maxint就是这个值，这里就是随便找个足够大的值。
        # 原来的是这个数：sysMaxInt = 9223372036854775807，结果时间巨长。
        # 这次换个小的，代码不变（换成python3提交了- -）试试看。
        sysMaxInt = 1024102410241024

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
https://leetcode-cn.com/submissions/detail/78223152/

37 / 37 个通过测试用例
状态：通过
执行用时：2432 ms
内存消耗：17.8 MB
"""
