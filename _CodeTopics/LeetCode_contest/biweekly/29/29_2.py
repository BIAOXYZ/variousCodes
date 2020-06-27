class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
        # 因为n不超过1000，又有31*31=961，32*32=1024。
        # 所以循环到32就可以了。
        
        res = []
        maxSqrtRoot = 32
        for i in range(1, maxSqrtRoot):
            if n % i == 0:
                res.append(i)
                res.append(n/i)
        
        # 32只是最大可能，还是有可能有重复的（其实也可以用字典，但是回头再说了）
        res = set(res)
        res = list(res)
        if len(res) < k:
            return -1
        else:
            res.sort()
            return res[k-1]
        
"""
https://leetcode-cn.com/contest/biweekly-contest-29/submissions/detail/82515806/

207 / 207 个通过测试用例
	状态：通过
执行用时：24 ms
内存消耗：12.6 MB
"""
