class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 参考了官方答案的实现

        highestBitPos = 30
        res = 0

        for k in range(highestBitPos, -1, -1):
            se = set()
            for num in nums:
                se.add(num >> k)
            
            nextRes, found = 2*res + 1, False
            for num in nums:
                if nextRes ^ (num >> k) in se:
                    found = True
                    break
            if found:
                res = nextRes
            else:
                res = nextRes - 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/178070030/

39 / 39 个通过测试用例
状态：通过
执行用时: 240 ms
内存消耗: 14.4 MB

执行用时：240 ms, 在所有 Python 提交中击败了57.14%的用户
内存消耗：14.4 MB, 在所有 Python 提交中击败了95.24%的用户
"""
