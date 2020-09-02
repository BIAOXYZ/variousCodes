class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        alphabet = ['BLANK', 'SIGN', 'DIGIT', 'DOT', 'E', 'illegal-input']

        state = [
            'START', 'REFUSE',
            'blank-before', 'sign-for-num', 'digit-before-dot', 'dot', 'dot-without-num',
            'digit-after-dot', 'e-E', 'sign-for-e', 'digit-for-e', 'blank-after'
        ]
        
        # 艹，为什么小数点结尾也算合法？？？
        acceptState = [
            'digit-before-dot', 'dot', 'digit-after-dot',
            'digit-for-e', 'blank-after'
            ]

        # stt: State Transition Table
        # https://en.wikipedia.org/wiki/State-transition_table    
        stt = {
            'START':{
                'BLANK':'blank-before',
                'DIGIT':'digit-before-dot',
                'DOT':'dot-without-num',
                'SIGN':'sign-for-num'
                },
            'blank-before':{
                'BLANK':'blank-before',
                'DIGIT':'digit-before-dot',
                'DOT':'dot-without-num',
                'SIGN':'sign-for-num'
            },
            'sign-for-num':{
                'DIGIT':'digit-before-dot',
                'DOT':'dot-without-num'
            },
            'digit-before-dot':{
                'DIGIT':'digit-before-dot',
                'DOT':'dot',
                'E':'e-E',
                'BLANK':'blank-after'
            },
            'dot':{
                'DIGIT':'digit-after-dot',
                'E':'e-E',
                'BLANK':'blank-after'
            },
            'dot-without-num':{
                'DIGIT':'digit-after-dot'
            },
            'digit-after-dot':{
                'DIGIT':'digit-after-dot',
                'E':'e-E',
                'BLANK':'blank-after'
            },
            'e-E':{
                'DIGIT':'digit-for-e',
                'SIGN':'sign-for-e'
            },
            'sign-for-e':{
                'DIGIT':'digit-for-e'
            },
            'digit-for-e':{
                'DIGIT':'digit-for-e',
                'BLANK':'blank-after'
            },
            'blank-after':{
                'BLANK':'blank-after'
            }
        }

        def transformInput(ch):
            if ch.isdigit(): return 'DIGIT'
            elif ch.lower() == "e": return 'E'
            elif ch == ".": return 'DOT'
            elif ch == "+" or ch == "-": return 'SIGN'
            elif ch == ' ': return 'BLANK'
            else: return 'illegal-input'

        st = 'START'
        for ch in s:
            inputst = transformInput(ch)
            if inputst not in stt[st]:
                return False
            st = stt[st][inputst]
        
        return st in acceptState
        
"""
https://leetcode-cn.com/submissions/detail/104232759/

1480 / 1480 个通过测试用例
状态：通过
执行用时: 40 ms
内存消耗: 12.7 MB
"""
"""
执行用时：40 ms, 在所有 Python 提交中击败了42.69%的用户
内存消耗：12.7 MB, 在所有 Python 提交中击败了52.67%的用户
"""
