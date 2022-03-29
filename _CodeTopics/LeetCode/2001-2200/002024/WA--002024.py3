class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        # 个人的想法是“巨型滑动窗口”：
        # 1. 如果 T 或 F 的数量还达不到 k 个，那答案就是整个字符串的长度。
        # 2. 如果 T 或 F 的数量都大于 k 个，那么就以连续的 k 个 T 换成 F
        #    或者 k 个 F 换成 T，遍历求出来换完后的最大的连续 F 或 T 的长度。

        n = len(answerKey)
        nT, nF = answerKey.count('T'), answerKey.count('F')
        if nT <= k or nF <= k:
            return n
        
        indT = [i for i in range(n) if answerKey[i] == 'T']
        indF = [i for i in range(n) if answerKey[i] == 'F']
        res = 0
        # 这里主要是为了好处理首尾的 index。
        indT = [-1] + indT + [n]
        indF = [-1] + indF + [n]

        for i in range(1, nT+1-k):
            pre, nxt = indT[i-1], indT[i+k]
            currLen = (nxt-1) - (pre+1) + 1
            res = max(res, currLen)
        for i in range(1, nF+1-k):
            pre, nxt = indF[i-1], indF[i+k]
            currLen = (nxt-1) - (pre+1) + 1
            res = max(res, currLen)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/291740558/

90 / 93 个通过测试用例
状态：解答错误

输入：
"FFFTTFTTFT"
3
输出：
7
预期结果：
8
"""
