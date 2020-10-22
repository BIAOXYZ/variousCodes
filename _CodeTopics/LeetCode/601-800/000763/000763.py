class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        res = []
        S = S + '#'
        length = len(S)

        left, right = 0, 1
        while right <= length - 1:
            while left != right:
                while S[left] in S[right:]:
                    if right == length - 1:
                        break
                    else:
                        right += 1
                left += 1
            res.append(right)
            right += 1

        for i in range(len(res)-1,0,-1):
            res[i] = res[i] - res[i-1]
        return res
        
"""
https://leetcode-cn.com/submissions/detail/117864114/

116 / 116 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 12.9 MB

执行用时：32 ms, 在所有 Python 提交中击败了45.30%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了5.97%的用户
"""
