class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """

        def mark_smallest_elem_to_false(lis):
            for elem in lis:
                if elem[1] == True:
                    elem[1] = False
                    return
            return res
        def pop_elem_with_false(lis):
            length = len(lis)
            for i in range(length-1, -1, -1):
                if lis[i][1] == False:
                    lis.pop(i)

        lisR, lisD = [], []
        for i in range(len(senate)):
            if senate[i] == "R":
                lisR.append([i, True])
            else:
                lisD.append([i, True])
        
        while lisR and lisD:
            lenR, lenD = len(lisR), len(lisD)
            ptrR, ptrD = 0, 0
            while ptrR <= lenR - 1 or ptrD <= lenD - 1:
                while ptrR <= lenR - 1 and lisR[ptrR][1] != True:
                    ptrR += 1
                while ptrD <= lenD - 1 and lisD[ptrD][1] != True:
                    ptrD += 1
                if ptrR > lenR - 1 and ptrD <= lenD -1:
                    ptrD += 1; mark_smallest_elem_to_false(lisR)
                elif ptrD > lenD - 1 and ptrR <= lenR -1:
                    ptrR += 1; mark_smallest_elem_to_false(lisD)
                else:
                    if ptrR <= lenR - 1 and ptrD <= lenD - 1:
                        if lisR[ptrR][0] < lisD[ptrD][0]:
                            ptrR += 1; mark_smallest_elem_to_false(lisD)
                        else:
                            ptrD += 1; mark_smallest_elem_to_false(lisR)
            pop_elem_with_false(lisR)
            pop_elem_with_false(lisD)
        return "Radiant" if lisR else "Dire"
        
"""
https://leetcode-cn.com/submissions/detail/130409653/

7 / 81 个通过测试用例
状态：执行出错

执行出错信息：
Line 13: NameError: global name 'res' is not defined
最后执行的输入：
"RDR"
"""
