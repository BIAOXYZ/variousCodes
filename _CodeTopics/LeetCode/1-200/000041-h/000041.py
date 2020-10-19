class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)

        # 把数组里的0和负数都变成length+1。这里如果变成None，后面处理可能要麻烦得多。
        for i in range(length):
            if nums[i] <= 0:
                nums[i] = length + 1
        
        for i in range(length):
            if abs(nums[i]) <= length:
                # nums[abs(nums[i])-1] *= -1
                # 原来上面那句在输入是[1,1]的时候会把最开始的位置标成-1，然后又标回1，导致出错。
                # 所以这里真的得老老实实地用下面这句
                nums[abs(nums[i])-1] = -abs(nums[abs(nums[i])-1])

        for i in range(length):
            if nums[i] > 0:
                return i + 1
        return length + 1

"""
https://leetcode-cn.com/submissions/detail/82439316/

165 / 165 个通过测试用例
状态：通过
执行用时：20 ms
内存消耗：12.6 MB
"""
