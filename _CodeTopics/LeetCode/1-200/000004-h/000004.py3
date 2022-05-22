class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # 参考了官方答案二分查找的解析和实现，此外还参考了这个帖子：
        # https://leetcode.cn/problems/median-of-two-sorted-arrays/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-w-2/
        # 最终综合两个一起写成下面的这个。

        def get_kth_element(k, start1, start2):
            # 如果第一个数组已经用完了
            if start1 >= m:
                return nums2[start2 + k - 1]
            # 如果第二个数组已经用完了
            elif start2 >= n:
                return nums1[start1 + k - 1]
            # 只需要比较 1 个时候
            elif k == 1:
                return min(nums1[start1], nums2[start2])
            else:
                end1 = min(start1 + k//2 - 1, m - 1)
                end2 = min(start2 + k//2 - 1, n - 1)
                if nums1[end1] <= nums2[end2]:
                    k -= end1 - start1 + 1
                    newStart1 = end1 + 1
                    return get_kth_element(k, newStart1, start2)
                else:
                    k -= end2 - start2 + 1
                    newStart2 = end2 + 1
                    return get_kth_element(k, start1, newStart2)
        
        m, n = len(nums1), len(nums2)
        totalLen = m + n
        # 两个数组起始的 index 当然都是 0。
        index1, index2 = 0, 0
        if totalLen % 2 == 1:
            return get_kth_element((totalLen + 1) // 2, index1, index2)
        else:
            first = get_kth_element(totalLen//2, index1, index2)
            second = get_kth_element(totalLen//2 + 1, index1, index2)
            return (first + second) / 2
        
"""
https://leetcode.cn/submissions/detail/316879101/

执行用时：
48 ms
, 在所有 Python3 提交中击败了
66.02%
的用户
内存消耗：
16 MB
, 在所有 Python3 提交中击败了
5.07%
的用户
通过测试用例：
2094 / 2094
"""
