class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:

        # 参考了官方答案，基本一样了。但是开始时有个点想不通：我一直觉得以 nums[i] 为最小值
        # 的子数组的数量应该是 (k−i+1) × (i−j+1)，而不是官方答案里的 (k−i) × (i−j)。
        # 直到后来综合了下面这两个链接（主要是第一个链接吧）才明白是我开闭区间搞混了。
        # https://leetcode-cn.com/problems/sum-of-subarray-ranges/solution/daydayuppp-dan-diao-zhan-on-zuo-fa-by-da-pmmt/
        # https://leetcode-cn.com/problems/sum-of-subarray-ranges/solution/tong-ge-lai-shua-ti-la-yi-ti-san-jie-bao-sfas/

        n = len(nums)

        minLeft, maxLeft = [0 for _ in range(n)], [0 for _ in range(n)]
        minStack, maxStack = [], []
        for i, num in enumerate(nums):
            while minStack and nums[minStack[-1]] > num:
                minStack.pop()
            minLeft[i] = minStack[-1] if minStack else -1
            minStack.append(i)

            # 这里要用 <= 了，因为按答案规定了如果两个数相等，下标小的算逻辑上更小的。
            while maxStack and nums[maxStack[-1]] <= num:
                maxStack.pop()
            maxLeft[i] = maxStack[-1] if maxStack else -1
            maxStack.append(i)
        
        minRight, maxRight = [0 for _ in range(n)], [0 for _ in range(n)]
        minStack, maxStack = [], []
        for i in range(n-1, -1, -1):
            num = nums[i]
            while minStack and nums[minStack[-1]] >= num:
                minStack.pop()
            minRight[i] = minStack[-1] if minStack else n
            minStack.append(i)

            while maxStack and nums[maxStack[-1]] < num:
                maxStack.pop()
            maxRight[i] = maxStack[-1] if maxStack else n
            maxStack.append(i)
        
        sumMax, sumMin = 0, 0
        for i in range(n):
            sumMax += (maxRight[i] - i) * (i - maxLeft[i]) * nums[i]
            sumMin += (minRight[i] - i) * (i - minLeft[i]) * nums[i]
        return sumMax - sumMin
        
"""
https://leetcode-cn.com/submissions/detail/277461642/

执行用时：72 ms, 在所有 Python3 提交中击败了88.77%的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了35.10%的用户
通过测试用例：
71 / 71
"""
