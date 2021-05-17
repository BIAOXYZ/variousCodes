class Solution(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        # 此前曾为第 188 周周赛第二题
        # https://leetcode-cn.com/contest/weekly-contest-188/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/

        def isLegal(i, j, k):
            return prefixXor[j] ^ prefixXor[i] == prefixXor[k+1] ^ prefixXor[j]

        length = len(arr)
        prefixXor = [0]
        for i in range(length):
            prefixXor.append(prefixXor[-1] ^ arr[i])
        
        res = 0
        for i in range(length-1):
            for j in range(i+1, length):
                for k in range (j, length):
                    if isLegal(i,j,k):
                        res += 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/178451598/

47 / 47 个通过测试用例
状态：通过
执行用时: 3972 ms
内存消耗: 12.8 MB

执行用时：3972 ms, 在所有 Python 提交中击败了9.09%的用户
内存消耗：12.8 MB, 在所有 Python 提交中击败了81.82%的用户
"""
