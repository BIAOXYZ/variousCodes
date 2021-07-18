import bisect
class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # 第 238 周周赛第二题。
        # 基于该提交 https://leetcode-cn.com/submissions/detail/171672276/ 修改。

        """
        # 想用前缀和，但是下面这些代码好像还有些问题。
        # 只好先简单优化下过去提交那个版本，去掉while循环试试。

        n = len(newnum)
        prefixTotalDiff = [0] * n
        totalElemNum = [0] * n
        for i in range(n-1, 0, -1):
            distance = newnum[i] - newnum[i-1] 
            prefixTotalDiff[i] = prefixTotalDiff[i-1] + ctr[newnum[i-1]] * distance
            totalElemNum[i] = totalElemNum[i-1] + ctr[newnum[i-1]]
        
        res = 0
        for i in range(1, n):
            tmp = 0
            tmpk = k
            ind = bisect.bisect_right(prefixTotalDiff, k)
            tmp += totalElemNum[ind-1]
            tmpk -= prefixTotalDiff[i-1]
            while tmpk >= 
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
                    tmp += tmpk / (newnum[i] - newnum[j])
                    break
            incr[i] = tmp + ctr[newnum[i]]
        return max(incr)
        
"""
https://leetcode-cn.com/submissions/detail/197230036/

62 / 71 个通过测试用例
状态：超出时间限制
"""
