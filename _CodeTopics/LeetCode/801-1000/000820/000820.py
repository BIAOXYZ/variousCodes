class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        # 感觉trivial的二重for循环应该会超时。。。看着有点像字典树，但是用字典树解决问题的题目还碰得很少。

        words = list(set(words))
        words.sort(key = lambda x : len(x))
        res = 0
        for i in range(len(words)-1):
            needPlus = True
            for j in range(i+1, len(words)):
                shortStr, LongStr = words[i], words[j]
                if LongStr.endswith(shortStr):
                    needPlus = False
                    break
            if needPlus:
                res += len(shortStr) + 1
        res += len(words[-1]) + 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/202108768/

36 / 36 个通过测试用例
状态：通过
执行用时: 4420 ms
内存消耗: 13.7 MB

执行用时：4420 ms, 在所有 Python 提交中击败了13.51%的用户
内存消耗：13.7 MB, 在所有 Python 提交中击败了27.03%的用户
"""
