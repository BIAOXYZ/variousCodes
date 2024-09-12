class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:

        """
        # 以 [9,2,5,4] 为例，排序后为 [2,4,5,9]。排序后的结果分成前一半和后一半。
          能被标记的下标可以分为“小值”和“大值”，那么一个关键的点是：
        # 小值只能出现在前一半，大值只能出现在后一半，否则没有意义！
          比如想把 5 作为小值是没意义的，因为肯定有比它更好的能当小值的。
        # 类似的道理，如果数组长度是奇数，最中间那个数是没有用的：
          作小值吧，前一半里哪个都比它小；作大值吧，后一半里哪个都比它大。
        # while 条件只需要考虑大的那一半的那个指针就行。
        """

        n = len(nums)
        if n == 1:
            return 0
        
        if n & 1 == 0:
            ptr_small, ptr_large = 0, n//2
        else:
            ptr_small, ptr_large = 0, n//2 + 1

        nums.sort()
        res = 0
        while ptr_large <= n - 1:
            if nums[ptr_small] * 2 <= nums[ptr_large]:
                res += 2
                ptr_small += 1
            ptr_large += 1
        return res

"""
https://leetcode.cn/problems/find-the-maximum-number-of-marked-indices/submissions/563984418/?envType=daily-question&envId=2024-09-12

通过
零知识证明
零知识证明
提交于 2024.09.12 13:19

执行用时分布
139
ms
击败
69.30%
消耗内存分布
30.05
MB
击败
42.79%
"""
