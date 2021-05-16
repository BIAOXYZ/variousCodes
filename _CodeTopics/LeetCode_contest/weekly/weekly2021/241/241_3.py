class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        nums1.sort()
        self.nums1 = nums1
        self.nums2 = nums2
        self.ctr = collections.Counter(nums2)


    def add(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.ctr[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.ctr[self.nums2[index]] = self.ctr.setdefault(self.nums2[index], 0) + 1
        

    def count(self, tot):
        """
        :type tot: int
        :rtype: int
        """
        res = 0
        for i, n1 in enumerate(self.nums1):
            if tot - n1 in self.ctr: 
                res += self.ctr[tot-n1]
        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)

"""
https://leetcode-cn.com/submissions/detail/177899971/

25 / 25 个通过测试用例
状态：通过
执行用时: 1120 ms
内存消耗: 33.4 MB
"""
