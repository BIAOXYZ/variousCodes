class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 参考了官方 C++ 的分治（线段树）实现。只不过把 C++ 的结构体改成了字典。
        # 当然用list写起来更简单，但是后面看稍麻烦。

        def pushUp(left, right):
            dic = {
                'totalSum': left['totalSum'] + right['totalSum'],
                'l_start_Sum': max(left['l_start_Sum'], left['totalSum'] + right['l_start_Sum']),
                'r_end_Sum': max(right['r_end_Sum'], right['totalSum'] + left['r_end_Sum']),
                'resSum': max(left['resSum'], right['resSum'], left['r_end_Sum'] + right['l_start_Sum'])
            }
            return dic

        def get_status(arr, leftIndex, rightIndex):
            if leftIndex == rightIndex:
                return {'totalSum':arr[leftIndex], 'l_start_Sum':arr[leftIndex], 'r_end_Sum':arr[leftIndex], 'resSum':arr[leftIndex]}
            mid = (leftIndex + rightIndex) / 2
            ldic = get_status(arr, leftIndex, mid)
            rdic = get_status(arr, mid + 1, rightIndex)
            return pushUp(ldic, rdic)
        
        return get_status(nums, 0, len(nums)-1)['resSum']
        
"""
https://leetcode-cn.com/submissions/detail/196904683/

202 / 202 个通过测试用例
状态：通过
执行用时: 132 ms
内存消耗: 15.2 MB

执行用时：132 ms, 在所有 Python 提交中击败了5.33%的用户
内存消耗：15.2 MB, 在所有 Python 提交中击败了89.60%的用户
"""
