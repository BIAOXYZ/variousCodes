class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """

        def str_to_dict(s):
            dic = {}
            for ch in s:
                if dic.has_key(ch):
                    dic[ch] += 1
                else:
                    dic[ch] = 1
            return dic

        length = len(s)
        dic = str_to_dict(s)
        monotoneStk = []

        for i in range(length):
            if s[i] not in monotoneStk:
                while monotoneStk and monotoneStk[-1] > s[i]:
                    if dic[monotoneStk[-1]] > 0:
                        monotoneStk.pop()
                    else:
                        break
                monotoneStk.append(s[i])
                dic[s[i]] -= 1
        return ''.join(monotoneStk)
        
"""
https://leetcode-cn.com/submissions/detail/132901979/

225 / 289 个通过测试用例
状态：解答错误

输入：
"bbcaac"
输出：
"ac"
预期：
"bac"
"""
