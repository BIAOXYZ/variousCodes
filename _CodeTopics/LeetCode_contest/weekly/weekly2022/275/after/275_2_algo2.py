class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        total_ones = nums.count(1)
        if total_ones == n or total_ones == 0: return 0
        window_len = total_ones
        
        # 不管怎么样，最终一定是要把所有1换到连在一起的。这里不管换的过程，
        # 而只是对可能的换的结果和原始的对比，找到0最少的那个。
        # 那些连在一起的1就是一个滑动窗口，只不过这个滑动窗口是环形的而已。
        
        window_ones = nums[:window_len].count(1)
        min_zeros = cur_zeros = total_ones - window_ones
        for start in range(1, n+1):
            if nums[(start - 1) % n] == 0:
                cur_zeros -= 1
            if nums[(start + window_len - 1) % n] == 0:
                cur_zeros += 1
            min_zeros = min(min_zeros, cur_zeros)
        return min_zeros
    
"""
https://leetcode-cn.com/submissions/detail/257052125/

63 / 63 个通过测试用例
状态：通过
执行用时: 144 ms
内存消耗: 17.4 MB
"""
