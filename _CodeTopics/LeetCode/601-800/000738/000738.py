class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """

        def has_increasing_digits(N):
            lis = int_to_list(N)
            if lis == sorted(lis):
                return True
            return False
        def int_to_list(N):
            lis = []
            while N > 0:
                lis.insert(0, N % 10)
                N /= 10
            return lis
        def list_to_int(lis):
            num = lis[0]
            length = len(lis)
            if length == 1:
                return num
            else:
                for i in range(1, length):
                    num = num * 10 + lis[i]
            return num

        if has_increasing_digits(N):
            return N
        
        lis = int_to_list(N)
        length = len(lis)
        replaceLeftNumsFlag = False 
        for i in range(1, length):
            if replaceLeftNumsFlag == True:
                lis[i] = 9
                continue
            if lis[i] < lis[i-1]:
                replaceLeftNumsFlag = True
                while i > 0 and lis[i] < lis[i-1]:
                    lis[i] = 9
                    lis[i-1] -= 1
                    i -= 1
        if lis[0] == 0:
            lis.pop(0)
        return list_to_int(lis)
        
"""
https://leetcode-cn.com/submissions/detail/131334698/

302 / 303 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 13 MB

执行用时：28 ms, 在所有 Python 提交中击败了25.00%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了23.26%的用户
"""
