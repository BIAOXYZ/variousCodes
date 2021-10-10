class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        
        dic, res = {}, set()
        for arr in [nums1, nums2, nums3]:
            arr = set(arr)
            for elem in arr:
                dic[elem] = dic.setdefault(elem, 0) + 1
                if dic[elem] >= 2:
                    res.add(elem)
        return list(res)
    
"""
https://leetcode-cn.com/submissions/detail/227322774/

288 / 288 个通过测试用例
状态：通过
执行用时: 36 ms
内存消耗: 12.9 MB
"""
