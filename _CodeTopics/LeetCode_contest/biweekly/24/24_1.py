class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        startValue = 1
        sum = startValue
        for num in nums:
            sum = sum + num
            if sum <= 0:
                startValue = startValue + 1 - sum
                sum = 1
        return startValue
  
