class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """

        # 类似答案的算法：先不断分治，每一次分治完成后做归并排序，使得上一层更好处理。
        def divide_and_conquer_with_merge_sort(left, right):
            if left == right:
                return 0
            else:
                mid = (left + right) / 2
                tmpres = divide_and_conquer_with_merge_sort(left, mid) + divide_and_conquer_with_merge_sort(mid+1, right)

            i = left
            le, ri = mid + 1, mid + 1
            while i <= mid:
                while le <= right and prefixSum[le] - prefixSum[i] < lower:
                    le += 1
                # 这里 <= upper 我感觉应该用 < 也行啊，但是事实是不行。。。回头再看了。
                while ri <= right and prefixSum[ri] - prefixSum[i] <= upper:
                    ri += 1
                tmpres += ri - le
                i += 1
            
            # 两个小区间的计算完成后，就用归并排序合并，从而方便更上一层大区间计算。
            newInterval = [0 for _ in range(right-left+1)]
            p1, p2, p = left, mid + 1, 0
            while p1 <= mid or p2 <= right:
                if p1 > mid:
                    newInterval[p] = prefixSum[p2]
                    p += 1; p2 += 1
                elif p2 > right:
                    newInterval[p] = prefixSum[p1]
                    p += 1; p1 += 1
                else:
                    if prefixSum[p1] < prefixSum[p2]:
                        newInterval[p] = prefixSum[p1]
                        p += 1; p1 += 1
                    else:
                        newInterval[p] = prefixSum[p2]
                        p += 1; p2 += 1
            for i in range(right-left+1):
                prefixSum[left+i] = newInterval[i]
            return tmpres

        length = len(nums)
        prefixSum = [0 for _ in range(length+1)]
        for i in range(1, length+1):
            prefixSum[i] = prefixSum[i-1] + nums[i-1]

        res = divide_and_conquer_with_merge_sort(0, length)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/121747657/

61 / 61 个通过测试用例
状态：通过
执行用时: 228 ms
内存消耗: 14.6 MB

执行用时：228 ms, 在所有 Python 提交中击败了32.35%的用户
内存消耗：14.6 MB, 在所有 Python 提交中击败了20.59%的用户
"""
