
####################################################################################################
####################################################################################################

class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """

        # 草，我就服了，基本就一样的代码，为啥我的总超时
        length = len(T)
        res = [0 for i in range(length)]
        monotonicStack = []

        for i in range(length):
            # 其实这个分支也就i等于0的时候会走一次。
            if monotonicStack == []:
                monotonicStack.append(i)
            for j in range(len(monotonicStack)-1,-1,-1):
                if T[i] > T[monotonicStack[j]]:
                    res[monotonicStack[j]] = i - monotonicStack[j]
                    monotonicStack.pop()
                    if monotonicStack == []:
                        monotonicStack.append(i)
                # T[i] 小于或者等于 T[monotonicStack[j]] 时都是一样的贴进去单调栈里，
                # 所以共用这一个else分支。
                else:
                    monotonicStack.append(i)
                    break
        return res

"""
https://leetcode-cn.com/submissions/detail/78864231/

34 / 37 个通过测试用例
状态：超出时间限制

最后执行的输入：[71,76,71,76,71,76,76,71,76,71,71,71,76,76,76,76,71,76,76,76,71,76,71,76,76,76,71,71,76,76,76,71,71,71,76,71,76,7...
"""

####################################################################################################

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        
        length = len(T)
        res = [0 for i in range(length)]
        monotonicStack = []

        for i in range(length):
            # 其实这个分支也就i等于0的时候会走一次。
            if monotonicStack == []:
                monotonicStack.append(i)
            for j in range(len(monotonicStack)-1,-1,-1):
                if T[i] > T[monotonicStack[j]]:
                    res[monotonicStack[j]] = i - monotonicStack[j]
                    monotonicStack.pop()
                    if monotonicStack == []:
                        monotonicStack.append(i)
                # T[i] 小于或者等于 T[monotonicStack[j]] 时都是一样的贴进去单调栈里，
                # 所以共用这一个else分支。
                else:
                    monotonicStack.append(i)
                    break
        return res

"""
https://leetcode-cn.com/submissions/detail/78864752/

37 / 37 个通过测试用例
状态：通过
执行用时：668 ms
内存消耗：17.9 MB
"""

####################################################################################################

