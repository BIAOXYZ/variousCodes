class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        def str_to_bit_map(s):
            res = ['0'] * 26
            for ch in s:
                ind = ord(ch) - ord('a')
                res[ind] = '1'
            tmp = ''.join(res)
            return tmp

        lens = map(len, words)
        words = map(str_to_bit_map, words)

        # 这里转整数不知道为什么有问题（末尾有个L，是长整型，但是你结果都没转对啊），服了！
        # 只好下面先用字符串来比，没用与操作。
        # w = map(int, words)

        res = 0
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if all(words[i][k] != words[j][k] or words[i][k] == words[j][k] == '0' for k in range(26)):
                    res = max(res, lens[i] * lens[j])
        return res
        
"""
https://leetcode-cn.com/submissions/detail/239374837/

执行用时：2676 ms, 在所有 Python 提交中击败了6.52%的用户
内存消耗：13.8 MB, 在所有 Python 提交中击败了19.57%的用户
通过测试用例：
167 / 167
"""
