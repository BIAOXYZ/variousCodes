class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        
        def is_legal_subarray(lis):
            n = len(lis)
            if n == 2:
                if lis[0] == lis[1]:
                    return True
            elif n == 3:
                if lis[0] == lis[1] == lis[2]:
                    return True
                if lis[1] == lis[0] + 1 and lis[2] == lis[1] + 1:
                    return True
            return False

        memoDic = {}
        def memorize_search(lis, start_pos):
            if start_pos in memoDic:
                return memoDic[start_pos]
            n = len(lis)
            if start_pos == n:
                memoDic[start_pos] = True
            elif start_pos == n - 1:
                memoDic[start_pos] = False
            elif start_pos == n - 2:
                memoDic[start_pos] = lis[start_pos] == lis[start_pos + 1]
            else:
                memoDic[start_pos] = ( is_legal_subarray(lis[start_pos:start_pos+2]) and memorize_search(lis, start_pos+2) ) or \
                    ( is_legal_subarray(lis[start_pos:start_pos+3]) and memorize_search(lis, start_pos+3) )
            return memoDic[start_pos]
        
        return memorize_search(nums, 0)
       
"""
https://leetcode.cn/problems/check-if-there-is-a-valid-partition-for-the-array/submissions/516568491?envType=daily-question&envId=2024-03-01

通过

执行用时分布
208
ms
击败
13.43%
使用 Python3 的用户
消耗内存分布
51.77
MB
击败
15.91%
使用 Python3 的用户
"""
"""
相比 https://github.com/BIAOXYZ/variousCodes/blob/master/_CodeTopics/LeetCode/2201-2400/002369/MLE--002369.py3，这个能过的主要原因就是记忆化搜索的时候不传切片了，只传索引。
"""
