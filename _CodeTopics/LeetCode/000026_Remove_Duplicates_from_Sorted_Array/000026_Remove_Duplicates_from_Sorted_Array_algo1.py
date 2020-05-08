class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 若不限制新申请的空间，可以新建一个空的结果列表，然后遍历nums：
        ## 若当前元素nums[i]不在结果列表中，就append进结果列表，然后下一个元素
        ## 若当前元素nums[i]在结果列表中，直接下一个元素

        # 但是限制空间，那么第一反应就是，对每一个元素num[i]，遍历整个nums，碰到相等的就in-place删除。
        ## 最后求完全去重后的nums的长度即可。
        ## 但是for循环过程中删除list元素可能会导致问题，一般都是采用倒着循环

        """
        # 我认为题目的描述并不好：返回值按照题目的描述应该就只是一个数值，即去重后的列表的长度就可以了。
        # 但是实际上要求的是返回去重后的列表。这也导致某些思路本来应该是可以的，但是实际上行不通。
        # 下面的代码就是每次都从第一个元素开始，把结果len加1，然后把所有这个元素删除，直到最后删成空列表。本来肯定是对的，但是在题目不咋滴的情况下就不对了。
        resLen = 0
        while nums != []:
            curr = nums[0]
            resLen += 1
            while curr in nums:
                nums.remove(curr)
        return resLen
        """

        if nums == []:
            return 0
        for i in range(len(nums)-1, 0, -1):
            if nums[i] == nums[i-1]:
                nums.pop(i)
        return len(nums)

"""
161 / 161 个通过测试用例
	状态：通过
执行用时：40 ms
内存消耗：14.6 MB
"""
