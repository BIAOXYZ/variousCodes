class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:

        # 回溯算法版本 —— 这次竟然是先想到位运算的。。。

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
        
        def backtrack(pos, tmpScore, tmpLetters):
            nonlocal res
            res = max(res, tmpScore)
            for i in range(pos, n):
                ctrWord = Counter(words[i])
                if all(tmpLetters[letter] + ctrWord[letter] <= ctr[letter] for letter in words[i]):
                    tmpScore += calculate_word_score(words[i], dic)
                    for letter in words[i]:
                        tmpLetters[letter] += 1
                    backtrack(i, tmpScore, tmpLetters)
                    tmpScore -= calculate_word_score(words[i], dic)
                    for letter in words[i]:
                        tmpLetters[letter] -= 1
        
        n = len(words)
        ctr = Counter(letters)
        dic = form_letter_score_dic(score)
        res = 0
        backtrack(0, 0, defaultdict(int))
        return res
        
"""
https://leetcode.cn/submissions/detail/406563122/

21 / 52 个通过测试用例
状态：解答错误

输入：
["add","dda","bb","ba","add"]
["a","a","a","a","b","b","b","b","c","c","c","c","c","d","d","d"]
[3,9,8,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
输出：
63
预期结果：
51
"""
