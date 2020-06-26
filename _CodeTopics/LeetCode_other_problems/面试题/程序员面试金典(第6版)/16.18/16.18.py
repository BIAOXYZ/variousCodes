class Solution(object):
    def patternMatching(self, pattern, value):
        """
        :type pattern: str
        :type value: str
        :rtype: bool
        """

        length = len(value)
        numa = pattern.count('a')
        numb = pattern.count('b')

        def check(lena, lenb):
            worda, wordb = [], []
            currind = 0
            for letter in pattern:
                if letter == 'a':
                    if value[currind:currind+lena] not in worda:
                        worda.append(value[currind:currind+lena])
                    currind += lena
                    if len(worda) >= 2:
                        return False
                else:
                    if value[currind:currind+lenb] not in wordb:
                        wordb.append(value[currind:currind+lenb])
                    currind += lenb
                    if len(wordb) >= 2:
                        return False
            return True
        
        if numa != 0 and numb != 0:
            if length == 0:
                return False
            for lena in range(length/numa + 1):
                for lenb in range((length-numa*lena)/numb + 1):
                    if numa*lena + numb*lenb == length:
                        if check(lena, lenb):
                            return True
        elif numa != 0 and numb == 0:
            for lena in range(length/numa + 1):
                if numa*lena == length:
                    if check(lena, 0):
                        return True
        elif numa == 0 and numb != 0:
            for lenb in range(length/numb + 1):
                if numb*lenb == length:
                    if check(0, lenb):
                        return True
        else:
            if value == '':
                return True
        return False

"""
https://leetcode-cn.com/submissions/detail/82253222/

93 / 93 个通过测试用例
状态：通过
执行用时：32 ms
内存消耗：12.7 MB
"""
"""
执行用时：32 ms, 在所有 Python 提交中击败了34.71%的用户
内存消耗：12.7 MB, 在所有 Python 提交中击败了100.00%的用户
"""
