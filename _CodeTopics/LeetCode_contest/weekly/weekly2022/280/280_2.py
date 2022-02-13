class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # 选定奇数index和偶数index中出现最多的数来当最终的数
        
        n = len(nums)
        if n == 1:
            return 0
        elif n == 2:
            return 0 if nums[0] != nums[1] else 1
            
        ctrOdd = Counter(nums[0:n:2])
        ctrEven = Counter(nums[1:n:2])
        ##print(ctrOdd, ctrEven)
        
        l1 = ctrOdd.items()
        l2 = ctrEven.items()
        l1.sort(reverse=True, key = lambda x : x[1])
        l2.sort(reverse=True, key = lambda x : x[1])
        ##print(l1,l2)
        
        # maxOddKey = max(ctrOdd, key=lambda x : ctrOdd[x])
        # maxEvenKey = max(ctrEven, key=lambda x : ctrEven[x])
        
        def calculate_step(k1, k2):
            step = 0
            for i in range(n):
                if i & 1 == 0 and nums[i] != k1:
                    step += 1
                if i & 1 == 1 and nums[i] != k2:
                    step += 1
            return step
        
        maxOddKey, maxEvenKey = l1[0][0], l2[0][0]
        if maxOddKey != maxEvenKey:
            return calculate_step(maxOddKey, maxEvenKey)
        else:
            if len(l1) == len(l2) == 1:
                return n / 2
            elif len(l1) == 1 and len(l2) >= 2:
                maxOddKey, maxEvenKey = l1[0][0], l2[1][0]
                return calculate_step(maxOddKey, maxEvenKey)
            elif len(l1) >= 2 and len(l2) == 1:
                maxOddKey, maxEvenKey = l1[1][0], l2[0][0]
                return calculate_step(maxOddKey, maxEvenKey)
            else:
                maxOddKey, maxEvenKey = l1[0][0], l2[1][0]
                steps1 = calculate_step(maxOddKey, maxEvenKey)
                maxOddKey, maxEvenKey = l1[1][0], l2[0][0]
                steps2 = calculate_step(maxOddKey, maxEvenKey)
                return min(steps1, steps2)
    
"""
https://leetcode-cn.com/submissions/detail/267696281/

127 / 127 个通过测试用例
状态：通过
执行用时: 436 ms
内存消耗: 35.4 MB
"""
