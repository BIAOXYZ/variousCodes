class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        # 今天是清明节假期看媳妇儿从西安返程（从洛阳龙门站回来的基本。。。），到住的地方没多久，赶紧搞一下。
        
        for i in range(-1, -n-1, -1):
            nums1[i] = nums2[i]
        nums1.sort()
        
"""
https://leetcode-cn.com/submissions/detail/164116933/

59 / 59 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 12.9 MB

执行用时：20 ms, 在所有 Python 提交中击败了64.43%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了73.66%的用户
"""
