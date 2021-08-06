class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        length = len(nums)
        if length == 1: return False
        
        currState = []
        for index in range(length):
            currState.append(index)
            nextIndex = (index + nums[index]) % length
            while nextIndex not in currState:
                currState.append(nextIndex)
                index += nums[index]
                nextIndex = (index + nums[index]) % length
            indOfFirstDupElem = currState.index(nextIndex)
            minDupList = currState[indOfFirstDupElem:]
            if len(minDupList) > 1 and (all(nums[ind] < 0 for ind in minDupList) or all(nums[ind] > 0 for ind in minDupList)):
                return True
            currState = []
        return False
        
"""
https://leetcode-cn.com/submissions/detail/204098833/

3 / 41 个通过测试用例
状态：执行出错

执行出错信息：
IndexError: list index out of range
    nextIndex = (index + nums[index]) % length
Line 18 in circularArrayLoop (Solution.py)
    ret = Solution().circularArrayLoop(param_1)
Line 46 in _driver (Solution.py)
    _driver()
Line 56 in <module> (Solution.py)
最后执行的输入：
[1,2,3,4,5]
"""
