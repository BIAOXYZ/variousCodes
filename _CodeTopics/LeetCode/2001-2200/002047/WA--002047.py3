class Solution:
    def countValidWords(self, sentence: str) -> int:

        lis = sentence.split()
        res = 0
        for w in lis:
            if all(not w[i].isdigit() for i in range(len(w))) and \
                (w.count('-') == 0 or (w.count('-') == 1 and w[0] != '-' and w[1] != '-')) and \
                (w.count('!') + w.count('.') + w.count(',') == 0 or \
                w.count('!') + w.count('.') + w.count(',') == 1 and w[-1] in ['!', '.', ',']):
                res += 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/262709956/

192 / 244 个通过测试用例
状态：解答错误

输入：
"b-a-c f-d"
输出：
0
预期结果：
1
"""
