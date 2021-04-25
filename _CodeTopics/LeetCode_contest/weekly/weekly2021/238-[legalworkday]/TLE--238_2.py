class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        ctr = collections.Counter(nums)
        newnum = list(set(nums))
        newnum.sort()
        
        n = len(newnum)
        incr = [0] * n
        for i in range(1, n):
            tmp = 0
            tmpk = k
            for j in range(i-1, -1, -1):
                if tmpk >= ctr[newnum[j]] * (newnum[i] - newnum[j]):
                    tmp += ctr[newnum[j]]
                    tmpk -= ctr[newnum[j]] * (newnum[i] - newnum[j])
                    continue
                else:
                    while tmpk >= newnum[i] - newnum[j]:
                        tmp += 1
                        tmpk -= newnum[i] - newnum[j]
            incr[i] = tmp + ctr[newnum[i]]
        return max(incr)
    
"""
https://leetcode-cn.com/submissions/detail/171672276/

62 / 65 个通过测试用例
状态：超出时间限制
提交时间：1 小时前
"""
