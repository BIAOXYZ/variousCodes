class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """

        length = len(arr)
        fracArr = []
        for i in range(length-1):
            for j in range(i+1, length):
                fracArr.append([arr[i], arr[j], arr[i]*1.0/arr[j]])
        
        fracArr.sort(key = lambda x : x[2])
        return [fracArr[k-1][0], fracArr[k-1][1]]
        
"""
https://leetcode-cn.com/submissions/detail/243281925/

执行用时：1900 ms, 在所有 Python 提交中击败了30.00%的用户
内存消耗：98.5 MB, 在所有 Python 提交中击败了30.00%的用户
通过测试用例：
59 / 59
"""
