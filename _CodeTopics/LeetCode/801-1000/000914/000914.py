class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """

        if len(deck) < 2:
            return False

        def list_to_dic_v2(lis):
            dic = {}
            for elem in lis:
                dic[elem] = dic.setdefault(elem, 0) + 1
            return dic
        dic = list_to_dic_v2(deck)
        freqList = dic.values()
        freqList.sort()

        # 所以其实是所有的频率的最大公约数只要大于1就可以，否则就不行。。。

        def gcd(a, b):
            if a < b:
                a, b = b, a
            while b != 0:
                a, b = b, a % b
            return a

        commomGCD = freqList[0]
        for i in range(1, len(freqList)):
            commomGCD = gcd(commomGCD, freqList[i])
            if commomGCD == 1:
                return False
        return True
        
"""
https://leetcode-cn.com/submissions/detail/201824073/

74 / 74 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13 MB

执行用时：24 ms, 在所有 Python 提交中击败了91.67%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了100.00%的用户
"""
