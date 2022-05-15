class Solution(object):
    def largestCombination(self, candidates):
        """
        :type candidates: List[int]
        :rtype: int
        """
        
        # 有点类似最长上升子序列，但是考虑到是有状态的（新的数得知道前面几个数的按位与结果），
        # 且输入长度上来看，动态规划的 O(n^2) 可能不行。
        
        n = len(candidates)
        ddic = defaultdict(int)
        for num in candidates:
            s = str(bin(num))[2:]
            s = s[::-1]
            ## print(num, s)
            for i, ch in enumerate(s):
                if ch == '1':
                    ddic[i] += 1
            ## print ddic
        return max(ddic.values())
        
"""
https://leetcode.cn/submissions/detail/313677505/

80 / 80 个通过测试用例
状态：通过
执行用时: 764 ms
内存消耗: 19.3 MB
"""
