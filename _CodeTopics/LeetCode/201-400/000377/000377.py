class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def factorial(n):
            res = 1
            for i in range(1, n+1):
                res *= i
            return res

        def cal_permutation_with_repeated_elems(lis):
            n = sum(lis)
            res = factorial(n)
            for num in lis:
                res /= factorial(num)
            return res

        def memorize_search(target):
            if dic.has_key(target):
                return dic[target]
            dic[target] = set()
            for num in nums:
                if target >= num:
                    for elem in memorize_search(target-num):
                        newElem = list(elem)
                        newElem[nums.index(num)] += 1
                        dic[target].add(tuple(newElem))
            return dic[target]
        
        basicList = [0 for _ in range(len(nums))]
        basicSet = set()
        basicSet.add(tuple(basicList))
        dic = {0:basicSet}
        memorize_search(target)

        res = 0
        for lis in dic[target]:
            res += cal_permutation_with_repeated_elems(lis)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/171467039/

15 / 15 个通过测试用例
状态：通过
执行用时: 928 ms
内存消耗: 76.7 MB

执行用时：928 ms, 在所有 Python 提交中击败了5.42%的用户
内存消耗：76.7 MB, 在所有 Python 提交中击败了5.42%的用户
"""
