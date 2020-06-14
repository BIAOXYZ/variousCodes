
####################################################################################################
# 现在看看，发现还是有些写得不好的地方的，比如:
# 1.第一个if分支，其实只有最开始单调栈monotonicStack为空的时候才会走进去一次，后面完全不可能再进去了。那么从
#   效率的角度出发，还是一上来就给单调栈把第一个元素贴进去，然后第一个for循环下标从1开始比较好。最开始没这么写
#   是觉得这么写不好看。。。
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

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        length = len(T)
        ans = [0] * length
        stack = []
        for i in range(length):
            temperature = T[i]
            while stack and temperature > T[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
        return ans
"""
# 官方答案
https://leetcode-cn.com/submissions/detail/78863818/

37 / 37 个通过测试用例
状态：通过
执行用时：548 ms
内存消耗：17.3 MB
"""
