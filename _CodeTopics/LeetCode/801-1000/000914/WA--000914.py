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
        for i in range(len(freqList)):
            if freqList[i] % freqList[0] != 0:
                return False
        return True
        
"""
https://leetcode-cn.com/submissions/detail/201818427/

45 / 74 个通过测试用例
状态：解答错误

最后执行的输入：
输入：
[1,1,1,1,2,2,2,2,2,2]
输出：
false
预期结果：
true
"""
