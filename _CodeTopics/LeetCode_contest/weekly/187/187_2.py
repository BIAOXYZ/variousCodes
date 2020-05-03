class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        indexlist = []
        for i in range(len(nums)):
            if nums[i] == 1:
                indexlist.append(i)
        
        for j in range(len(indexlist)-1):
            if indexlist[j+1] - indexlist[j] - 1 >= k:
                continue
            else:
                return False
        return True
    
"""
62 / 62 个通过测试用例
	状态：通过
执行用时：76 ms
内存消耗：19.8 MB
"""
