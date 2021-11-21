class Solution(object):
    def kMirror(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """
        
        def k_to_n(num, k):
            return int(str(num), base=k)
        ##print k_to_n(111, 2)

        def k_to_n_str(num, k):
            return int(num, base=k)

        def is_palindrome(s):
            left, right = 0, len(s)-1
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1 
            return True
        
        def get_new(currk):
            if all(currk[i] == str(k-1) for i in range(len(currk))):
                return '1' + '0' * (len(currk) - 1) + '1'
            else:
                left, right = 0, len(currk)-1
                while left <= right and currk[left] == str(k-1):
                    left += 1
                    right -= 1
                nextStr = str(int(currk[left])+1)
                if left != right:
                    return currk[:left] + nextStr + currk[left+1:right] + nextStr + currk[right+1:]
                else:
                    return currk[:left] + nextStr + currk[right+1:]
        
        res = 0
        currk = '1'
        currten = k_to_n_str(currk, k)
        while n > 0:
            while not is_palindrome(str(currten)):
                currk = get_new(currk)
                currten = k_to_n_str(currk, k)
            res += int(currten)
            n -= 1
            currk = get_new(currk)
            currten = k_to_n_str(currk, k)
        return res
"""
https://leetcode-cn.com/submissions/detail/240739899/

1 / 97 个通过测试用例
状态：超出时间限制

最后执行的输入：
3
7
"""
