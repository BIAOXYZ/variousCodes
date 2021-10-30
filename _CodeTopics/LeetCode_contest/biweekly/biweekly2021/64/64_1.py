from collections import Counter
class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        
        ctr = Counter(arr)
        se = set([key for key in ctr.keys() if ctr[key] == 1])
        tmp = 0
        for s in arr:
            if s in se:
                tmp += 1
                if tmp == k:
                    return s
        return ""
    
"""
https://leetcode-cn.com/submissions/detail/233885437/

65 / 65 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 13.2 MB
"""
