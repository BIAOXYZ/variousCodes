class Solution:
    def countValidWords(self, sentence: str) -> int:

        lis = sentence.split()
        res = 0
        for w in lis:
            if all(not w[i].isdigit() for i in range(len(w))) and \
                (w.count('-') == 0 or (w.count('-') == 1 and 0 < w.index('-') < len(w)-1 \
                    and w[w.index('-')-1].isalpha() and w[w.index('-')+1].isalpha())) and \
                (w.count('!') + w.count('.') + w.count(',') == 0 or \
                    (w.count('!') + w.count('.') + w.count(',') == 1 and w[-1] in '!.,')):
                res += 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/262710745/

执行用时：52 ms, 在所有 Python3 提交中击败了27.51%的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了22.63%的用户
通过测试用例：
244 / 244
"""
