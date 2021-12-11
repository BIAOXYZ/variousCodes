class Solution(object):
    def goodDaysToRobBank(self, security, time):
        """
        :type security: List[int]
        :type time: int
        :rtype: List[int]
        """
        
        n = len(security)
        if n < 2 * time + 1:
            return []
        
        leftinds = []
        leftind1 = 0
        inWindowState = False
        while leftind1 < n - 2*time:
            leftind2 = leftind1 + time
            if not inWindowState:
                breakflag = False
                for i in range(leftind1, leftind2):
                    if security[i] >= security[i+1]:
                        continue
                    else:
                        breakflag = True
                        leftind1 = i + 1
                        break
                if not breakflag:
                    inWindowState = True
                    leftinds.append(leftind1)
                    leftind1 += 1
            else:
                if security[leftind2 - 1] >= security[leftind2]:
                    leftinds.append(leftind1)
                    leftind1 += 1
                else:
                    inWindowState = False
                    leftind1 = leftind2
        ##print leftinds

        rightinds = []
        rightind1 = time
        inWindowState = False
        while rightind1 < n - time:
            rightind2 = rightind1 + time
            if not inWindowState:
                breakflag = False
                for i in range(rightind1, rightind2):
                    if security[i] <= security[i+1]:
                        continue
                    else:
                        breakflag = True
                        rightind1 = i + 1
                        break
                if not breakflag:
                    inWindowState = True
                    rightinds.append(rightind1 + 1)
                    rightind1 += 1
            else:
                if security[rightind2 - 1] <= security[rightind2]:
                    rightinds.append(rightind1 + 1)
                    rightind1 += 1
                else:
                    inWindowState = False
                    rightind1 = rightind2
        ##print rightinds        
        
        rightinds = set(rightinds)
        res = []
        for ind in leftinds:
            if ind + time + 1 in rightinds:
                res.append(ind + time)
        return res
    
"""
https://leetcode-cn.com/submissions/detail/247596451/

131 / 131 个通过测试用例
状态：通过
执行用时: 5416 ms
内存消耗: 31.3 MB
"""
