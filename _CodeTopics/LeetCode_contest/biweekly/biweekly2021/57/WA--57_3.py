class Solution(object):
    def splitPainting(self, segments):
        """
        :type segments: List[List[int]]
        :rtype: List[List[int]]
        """
        
        # 看来前两天做的差分数组+前缀和用上了。。。
        
        n = 10**5
        diff = [0 for _ in range(n+1)]
        
        for seg in segments:
            start, end, color = seg[0], seg[1], seg[2]
            diff[start] += color
            # 这里如果用 diff[end+1] -= color 很难处理，开始时就是用这个，各种问题
            diff[end] -= color
        
        prefixSum = [0]
        for i in range(1, n+1):
            prefixSum.append(prefixSum[-1] + diff[i])
        ##print prefixSum
        
        res = []
        left = 1
        for i in range(2, n+1):
            if prefixSum[i] == 0:
                res.append([left, i, prefixSum[left]])
                break
            if prefixSum[i] == prefixSum[left]:
                continue
            else:
                res.append([left, i, prefixSum[left]])
                left = i
        return res
    
"""
https://leetcode-cn.com/submissions/detail/199461974/

10 / 66 个通过测试用例
状态：解答错误

最后执行的输入：
输入：
[[1,4,5],[1,4,7],[4,7,1],[4,7,11]]
输出：
[[1,7,12]]
预期：
[[1,4,12],[4,7,12]]
"""
