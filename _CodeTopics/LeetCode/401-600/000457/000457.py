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
                nextIndex = (nextIndex + nums[nextIndex]) % length
            indOfFirstDupElem = currState.index(nextIndex)
            minDupList = currState[indOfFirstDupElem:]
            if len(minDupList) > 1 and (all(nums[ind] < 0 for ind in minDupList) or all(nums[ind] > 0 for ind in minDupList)):
                return True
            currState = []
        return False
        
"""
https://leetcode-cn.com/submissions/detail/204099328/

41 / 41 个通过测试用例
状态：通过
执行用时: 5492 ms
内存消耗: 13 MB

执行用时：5492 ms, 在所有 Python 提交中击败了8.33%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了70.83%的用户
"""
