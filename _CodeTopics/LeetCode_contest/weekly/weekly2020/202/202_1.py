class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        length = len(arr)
        currOddNum = 0
        for i in range(length):
            if arr[i] % 2 == 1:
                currOddNum += 1
                if currOddNum == 3:
                    return True
            else:
                currOddNum = 0
        return False
    
"""
https://leetcode-cn.com/submissions/detail/98520649/

31 / 31 个通过测试用例
状态：通过
执行用时：28 ms
内存消耗：12.9 MB
"""
