class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # 两个数组都带着索引排好序，然后对于 nums2 从大到小开始，如果当前 nums1 里的最大值能大于
        ## nums2 里的最大值，就用 nums1 里的最大值去匹配（根据贪心思想，这个是最佳方案）；
        ## 反之，就用 nums1 里的最小值去匹配。

        n = len(nums1)
        zip1 = list(zip(nums1, range(n)))
        zip2 = list(zip(nums2, range(n)))
        zip1.sort()
        zip2.sort()
        
        left, right = 0, n-1
        indexRelation = []
        for i in range(n-1, -1, -1):
            num2, ind2 = zip2[i]
            if zip1[right][0] > num2:
                indexRelation.append([zip1[right][1], ind2])
                right -= 1
            else:
                indexRelation.append([zip1[left][1], ind2])
                left += 1
        
        indexRelation.sort(key = lambda x: x[1])
        resInds = list(zip(*indexRelation))[0]
        ## print(zip1, zip2, indexRelation, resInds)
        return [nums1[ind] for ind in resInds]
        
"""
https://leetcode.cn/submissions/detail/370770330/

执行用时：
428 ms
, 在所有 Python3 提交中击败了
13.23%
的用户
内存消耗：
61 MB
, 在所有 Python3 提交中击败了
5.03%
的用户
通过测试用例：
67 / 67
"""
