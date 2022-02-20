class Solution(object):
    def repeatLimitedString(self, s, repeatLimit):
        """
        :type s: str
        :type repeatLimit: int
        :rtype: str
        """
        
        n = len(s)
        ctr = Counter(s)
        res = []
        alphabeta = 'zyxwvutsrqponmlkjihgfedcba'
        for i, ch in enumerate(alphabeta):
            if ch not in ctr:
                continue
            elif ctr[ch] <= repeatLimit:
                res.extend([ch] * ctr[ch])
                del ctr[ch]
            else:
                while ctr[ch] > repeatLimit:
                    res.extend([ch] * repeatLimit)
                    ctr[ch] -= repeatLimit
                    for j in range(i+1, 26):
                        ch2 = alphabeta[j]
                        if ch2 in ctr:
                            res.append(ch2)
                            ctr[ch2] -= 1
                            if ctr[ch2] == 0:
                                # 艹他大爷的，就这个 typo，找了半天！
                                # del ch2
                                del ctr[ch2]
                            break
                if ctr[ch] > 0 and res[-1] != ch:
                    res.extend([ch] * ctr[ch])
                    del ctr[ch]
        return ''.join(res)
    
"""
https://leetcode-cn.com/submissions/detail/270636810/

126 / 150 个通过测试用例
状态：解答错误

输入：
"bplpcfifosybmjxphbxdltxtfrjspgixoxzbpwrtkopepjxfooazjyosengdlvyfchqhqxznnhuuxhtbrojyhxwlsrklsryvmufoibgfyxgjw"
1
输出：
"zyzyzyxyxyxyxwxwxwxvxvxuxututststsrsrsrqrqrpopopopopopopononmnmlklkljljljijijijhghghghghfhfefefdfdfcfcbabbbb"
预期：
"zyzyzyxyxyxyxwxwxwxvxvxuxututststsrsrsrqrqrpopopopopopopononmnmlklkljljljijijijhghghghghfhfefefdfdfcfcbab"
"""
