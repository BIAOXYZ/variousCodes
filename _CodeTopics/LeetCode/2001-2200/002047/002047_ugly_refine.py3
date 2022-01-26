class Solution:
    def countValidWords(self, sentence: str) -> int:

        def valid_word(w):
            if all(not w[i].isdigit() for i in range(len(w))) and \
                (w.count('-') == 0 or (w.count('-') == 1 and 0 < w.index('-') < len(w)-1 \
                    and w[w.index('-')-1].isalpha() and w[w.index('-')+1].isalpha())) and \
                (total := w.count('!') + w.count('.') + w.count(',') == 0 or \
                    # 改成下面的一行还不行，会提示 “local variable 'total' referenced before assignment”
                    # (total == 1 and w[-1] in '!.,')):
                    # 所以相当于用 Assignment Expressions 改了个寂寞。。。
                    (w.count('!') + w.count('.') + w.count(',') == 1 and w[-1] in '!.,')):
                return True
            return False
        
        lis = sentence.split()
        res = 0
        for w in lis:
            res += 1 if valid_word(w) else 0
        return res
        
"""
https://leetcode-cn.com/submissions/detail/262711680/

执行用时：48 ms, 在所有 Python3 提交中击败了46.67%的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了5.15%的用户
通过测试用例：
244 / 244
"""
