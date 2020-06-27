class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        lenm = len(nums)
        posofzero = []
        for i in range(lenm):
            if nums[i] == 0:
                posofzero.append(i)
        
        length = len(posofzero)
        if length == 0 or length == 1:
            return lenm - 1
        else:
            # 如果不是上面那种简单的情况，就得具体去算了。由于可能是1开头或1结尾，
            # 为了不漏算就需要在首尾根据情况补0，这里就直接补在这个0的位置数组里就行。
            if nums[0] != 0:
                posofzero.insert(0,-1)
            if nums[lenm-1] != 0:
                posofzero.append(lenm)
            # 更新一下length，因为下面还要用。
            length = len(posofzero)
        ###print posofzero
         
        # 这个就是所有由0分割的全为1的子数组的长度，如果两个0紧挨着，那么认为其长度为0
        segmentlengthofone = []
        for i in range(length-1):
            segmentlengthofone.append(posofzero[i+1] - posofzero[i] - 1)
        ###print segmentlengthofone
        
        # 那么下面就是每两个相邻的相加一下，比一比，记下最大的返回就可以了。
        currlen = maxlen = 0
        for i in range(len(segmentlengthofone)-1):
            currlen = segmentlengthofone[i] + segmentlengthofone[i+1]
            maxlen = max(maxlen, currlen)
        return maxlen
    
"""
https://leetcode-cn.com/contest/biweekly-contest-29/submissions/detail/82531416/

73 / 73 个通过测试用例
	状态：通过
执行用时：36 ms
内存消耗：16.3 MB
"""
