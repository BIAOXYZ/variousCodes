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
        def memorize_search(lis, pos):
            if pos in memoDic:
                return memoDic[pos]
            n = len(lis)
            if n < 2:
                memoDic[pos] = True if n == 0 else False
            elif n == 2:
                memoDic[pos] = lis[0] == lis[1]
            else:
                memoDic[pos] = ( is_legal_subarray(lis[:2]) and memorize_search(lis[2:], pos+2) ) or \
                    ( is_legal_subarray(lis[:3]) and memorize_search(lis[3:], pos+3) )
            return memoDic[pos]
        
        return memorize_search(nums, 0)
        
"""
https://leetcode.cn/problems/check-if-there-is-a-valid-partition-for-the-array/submissions/516536567/?envType=daily-question&envId=2024-03-01

超出内存限制
64 / 118 个通过的测试用例
"""
"""
好久没做题，手生了很多，这个写的时间长，写的不好看，并且最后还爆内存了- -（但是算法倒是对了）。
以下还是 chatgpt 给指出的- -

这段代码中存在一个潜在的问题，导致内存使用过多。在 memorize_search 函数中递归调用的时候，每次传递 lis[2:] 或 lis[3:] 切片会导致新的列表对象被创建，消耗额外的内存空间。
在递归调用上层函数时，这些切片将保留在内存中，可能导致内存占用过高。
"""
