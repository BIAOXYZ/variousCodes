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

        #// 注：相比 `001838_algo2.py`，这个在细节上更接近与上面那个链接里的实现：也就是index计算时候的区别，对比下就知道了。
        length = len(nums)
        nums.sort()
        prefixSum = [nums[0]]
        for i in range(1, length):
            prefixSum.append(prefixSum[-1] + nums[i])

        maxFreq = 1
        for rightBoundary in range(1, length):
            low, high = 0, rightBoundary
            tmpInd = rightBoundary
            while low <= high:
                mid = (low + high) / 2
                #// 区别1
                total = (rightBoundary - mid + 1) * nums[rightBoundary]
                # 这里要防止下 mid 为 0 时一下子减到倒数第一个元素这种意外情况。
                #// 区别2
                prefixSum_mid_to_rightBountry = prefixSum[rightBoundary] - prefixSum[mid-1] if mid > 0 else prefixSum[rightBoundary] - 0
                distance = total - prefixSum_mid_to_rightBountry
                if distance > k:
                    low = mid + 1
                elif distance < k:
                    tmpInd = mid
                    high = mid - 1
                else:
                    tmpInd = mid
                    break
            maxFreq = max(maxFreq, rightBoundary - tmpInd + 1)
        return maxFreq
        
"""
https://leetcode-cn.com/submissions/detail/201225919/

71 / 71 个通过测试用例
状态：通过
执行用时: 2728 ms
内存消耗: 23.4 MB

执行用时：2728 ms, 在所有 Python 提交中击败了5.14%的用户
内存消耗：23.4 MB, 在所有 Python 提交中击败了5.91%的用户
"""
