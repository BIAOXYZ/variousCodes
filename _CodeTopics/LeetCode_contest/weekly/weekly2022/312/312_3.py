class Solution(object):
    def goodIndices(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        # 找波谷，但是 trivial 的方法 O(n^2) 肯定超时了。
        # 应该是先两侧各计算一下，分别找到 k 长的满足条件的左右半边，记录一下。
        # 然后可能的波谷位置 range(k, n-k) 循环检查一次就行。
        
        n = len(nums)
        l, r = [0]*n, [0]*n
        
        leftStart = 0
        while leftStart < n-k*2:
            if leftStart > 0 and l[leftStart-1] > 0 and nums[leftStart] <= nums[leftStart-1]:
                l[leftStart] = l[leftStart-1] - 1
                leftStart += 1
                continue
            l[leftStart] = 1
            for end in range(leftStart+1, n):
                if nums[end] <= nums[end-1]:
                    l[leftStart] += 1
                else:
                    break
            leftStart += 1
        ##print l
        
        rightStart = k + 1
        while rightStart < n-k+1:
            if rightStart > k+1 and r[rightStart-1] > 0 and nums[rightStart] >= nums[rightStart-1]:
                r[rightStart] = r[rightStart-1] - 1
                rightStart += 1
                continue
            r[rightStart] = 1
            for end in range(rightStart+1, n):
                if nums[end] >= nums[end-1]:
                    r[rightStart] += 1
                else:
                    break
            rightStart += 1
        ##print r
        
        res = []
        for center in range(k, n-k):
            left, right = center - k, center + 1
            if l[left] >= k and r[right] >= k:
                res.append(center)
        return res
    
"""
https://leetcode.cn/submissions/detail/366938932/

66 / 66 个通过测试用例
状态：通过
执行用时: 288 ms
内存消耗: 32.1 MB
"""
