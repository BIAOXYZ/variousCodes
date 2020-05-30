class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        
        l = list()
        for i in range(len(s)-k+1):
            # int第二个参数2是指把字符串按其二进制形式转
            num = int(s[i:i+k], 2)
            if num in l:
                continue
            else:
                l.append(num)
        
        # 其实可以不用字典，直接用列表，然后求和就好。和字典加key然后判断key在不在类似。
        sum = (2**k-1)*(2**(k-1))   # [(末项+首项)*项数]÷2 即：sum = (0 + 2**k-1)*(2**k)/2
        for num in l:
            sum -= num 
        if sum != 0:
            return False
        else:
            return True
        
"""
# https://leetcode-cn.com/submissions/detail/75006155/

183 / 196 个通过测试用例
	状态：解答错误

输入： "0110"
       2
输出： true
预期： false
"""
