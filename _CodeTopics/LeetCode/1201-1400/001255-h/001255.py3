class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:

        # 核心点就是条件里的那句 "单词表 words 中每个单词只能计分（使用）一次。"
        # 这一看，这个单词记分就是1，不计分就是0。再加上最多14个单词，那么：
        # 位运算来枚举，然后遍历统计没跑。

        def form_letter_score_dic(score):
            dic = {}
            for i in range(26):
                dic[chr(ord('a') + i)] = score[i]
            return dic

        def calculate_word_score(word, dic):
            res = 0
            for letter in word:
                res += dic[letter]
            return res
        
        n = len(words)
        ctr = Counter(letters)
        dic = form_letter_score_dic(score)
        res = 0
        for bitmap in range(2**n):
            tmpScore = 0
            tmpLetters = defaultdict(int)
            isLegal = True
            for i in range(14):
                if bitmap & (2**i) == 0:
                    continue
                for letter in words[i]:
                    if tmpLetters[letter] < ctr[letter]:
                        tmpLetters[letter] += 1
                    else:
                        isLegal = False
                        break
                if isLegal:
                    tmpScore += calculate_word_score(words[i], dic)
                else:
                    break
            if isLegal:
                res = max(res, tmpScore)
        return res
        
"""
https://leetcode.cn/submissions/detail/406530989/

执行用时：
264 ms
, 在所有 Python3 提交中击败了
44.30%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
87.34%
的用户
通过测试用例：
52 / 52
"""
