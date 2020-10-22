class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        dic, res = dict(), []
        # 原始的情况末尾很难处理，于是试试看加一个分隔符，是不是就不用考虑那么多了。
        S = S + '#'
        length = len(S)
        if length == 1:
            return [1]

        left, right = 0, 1
        while right <= length - 1:
            while left != right:
                while S[left] in S[right:]:
                    if right == length - 1:
                        break
                    else:
                        right += 1
                if right == length - 1:
                    break
                left += 1
            res.append(right)
            right += 1
            ##print res

        for i in range(len(res)-1,0,-1):
            if i == len(res)-1:
                #res[i] = res[i] - res[i-1] + 1
                res[i] = res[i] - res[i-1]
            else:
                res[i] = res[i] - res[i-1]
        return res
        
"""
https://leetcode-cn.com/submissions/detail/117743909/

116 / 116 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 13.1 MB

执行用时：28 ms, 在所有 Python 提交中击败了69.61%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了5.97%的用户
"""
