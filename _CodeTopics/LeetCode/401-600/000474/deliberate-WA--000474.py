class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """

        # 这个本来第一反应是贪心，可惜发现不对。不过既然写完了，还是提一下吧，杯具。。。

        res = 0
        if m < n: flag = 0
        else: flag = 1
        
        if flag == 0:
            strs.sort(key = lambda x : x.count('0'), reverse=True)
            while m > 0:
                if strs and strs[-1].count('0') <= m:
                    res += 1
                    m -= strs[-1].count('0')
                    strs.pop()
                else:
                    break
            strs.sort(key = lambda x : x.count('1'), reverse=True)
            while n > 0:
                if strs and strs[-1].count('1') <= n:
                    res += 1
                    n -= strs[-1].count('1')
                    strs.pop()
                else:
                    break
        else:
            strs.sort(key = lambda x : x.count('1'), reverse=True)
            while n > 0:
                if strs and strs[-1].count('1') <= n:
                    res += 1
                    n -= strs[-1].count('1')
                    strs.pop()
                else:
                    break
            strs.sort(key = lambda x : x.count('0'), reverse=True)
            while m > 0:
                if strs and strs[-1].count('0') <= m:
                    res += 1
                    m -= strs[-1].count('0')
                    strs.pop()
                else:
                    break
        return res
        
"""
https://leetcode-cn.com/submissions/detail/184337323/

24 / 70 个通过测试用例
状态：解答错误

最后执行的输入：
["10","0001","111001","1","0"]
5
3
输出
5
预期结果
4
"""
