class Solution(object):
    def constructDistancedSequence(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        # 应该是回溯算法 + 贪心思想
        
        res = [0 for _ in range(2*n - 1)]
        resList = []
        
        def backtrack(num):
            if num == 1:
                lastZeroInd = res.index(0)
                res[lastZeroInd] = 1
                resList.append(res[:])
                res[lastZeroInd] = 0
                return
            for ind in range(2*n - 1 - num):
                if res[ind] == 0 and res[ind + num] == 0:
                    res[ind] = res [ind+num] = num
                    backtrack(num - 1)
                    res[ind] = res [ind+num] = 0
        
        backtrack(n)
        # 这里挺奇怪的，按理说 resList[0] 就应该是最大的结果了啊，但是并不是。。。所以只好sort一下。
        resList.sort()
        return resList[-1]
    
"""
https://leetcode-cn.com/submissions/detail/137237888/

11 / 20 个通过测试用例
状态：超出时间限制

最后执行的输入：
13
"""
