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
        res.extend(lis)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/123292129/

6 / 16 个通过测试用例

提交时间：几秒前
输入：
[28,6,22,8,44,17]
[22,28,8,6]
输出：
[22,28,8,6,44,17]
预期：
[22,28,8,6,17,44]
"""
