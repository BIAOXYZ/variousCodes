class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """

        len1, len2 = len(arr1), len(arr2)
        dic, lis, res = {}, [], []

        for i in range(len1):
            if arr1[i] not in arr2:
                lis.append(arr1[i])
                continue
            if dic.has_key(arr1[i]):
                dic[arr1[i]] += 1
            else:
                dic[arr1[i]] = 1

        for num in arr2:
            for i in range(dic[num]):
                res.append(num)
        res.extend(sorted(lis))
        return res
        
"""
https://leetcode-cn.com/submissions/detail/123292237/

16 / 16 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.1 MB

执行用时：20 ms, 在所有 Python 提交中击败了97.35%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了16.82%的用户
"""
