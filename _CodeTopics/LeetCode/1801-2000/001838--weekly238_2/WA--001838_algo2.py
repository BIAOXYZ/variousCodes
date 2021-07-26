import bisect
class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # 第 238 周周赛第二题。
        # 修改较多，与周赛时的提交 https://leetcode-cn.com/submissions/detail/171672276/ 关系不是那么大了。 
        # 反倒是有一些参考（因为我基本也独立想到 “前缀和+二分” 了）了这个帖子（但是细节不一样）：
        # https://leetcode-cn.com/problems/frequency-of-the-most-frequent-element/solution/1838-zui-gao-pin-yuan-su-de-pin-shu-shua-ub57/
        # PS：这里的 left 和 right 里的 right 很容易造成误解，其实除了把for循环里过去的 i 改成 rightBoundary，
        #     更应该把这里的 left 和 right 改成 low 和 high 之类的。

        length = len(nums)
        nums.sort()
        prefixSum = [0] * length
        for i in range(1, length):
            prefixSum.append(prefixSum[-1] + nums[i])

        maxFrequency = 1
        for rightBoundary in range(1, length):
            left, right = 0, rightBoundary
            tmpInd = rightBoundary
            while left <= right:
                mid = (left + right) / 2
                distance = (right - mid) * nums[rightBoundary] - (prefixSum[rightBoundary] - prefixSum[mid])
                if distance > k:
                    left = mid + 1
                elif distance < k:
                    tmpInd = mid
                    right = mid - 1
                else:
                    break
            maxFrequency = max(maxFrequency, rightBoundary - mid + 1)
        return maxFrequency
        
"""
https://leetcode-cn.com/submissions/detail/200151890/

9 / 71 个通过测试用例
状态：解答错误

最后执行的输入：
[9940,9995,9944,9937,9941,9952,9907,9952,9987,9964,9940,9914,9941,9933,9912,9934,9980,9907,9980,9944,9910,9997]
7925
输出：
1
预期结果：
22
"""
