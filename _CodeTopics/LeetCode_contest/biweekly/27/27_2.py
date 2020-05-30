class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        
        dic = dict()
        for i in range(len(s)-k+1):
            num = int(s[i:i+k], 2)
            if dic.has_key(num):
                continue
            else:
                dic[num] = True
        
        # 这里是2**k，最开始写的是2**k-1，因为觉得比如k=3，那么就是0--7，取不到8。
        # 但是这里是range函数，本来就取不到！
        for i in range(2**k):
            if dic.has_key(i) == False:
                return False
        return True
    
"""
# https://leetcode-cn.com/contest/biweekly-contest-27/submissions/detail/75002199/

196 / 196 个通过测试用例
	状态：通过
执行用时：1072 ms
内存消耗：51.5 MB
"""
