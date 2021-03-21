class Solution(object):
    def getNumberOfBacklogOrders(self, orders):
        """
        :type orders: List[List[int]]
        :rtype: int
        """
        
        buydic = {}
        selldic = {}
        if orders[0][2] == 0:
            buydic[orders[0][0]] = orders[0][1]
        else:
            selldic[orders[0][0]] = orders[0][1]
        
        for i in range(1, len(orders)):
            od = orders[i]
            if od[2] == 0:
                tmp = sorted(selldic.keys(), reverse=True)
                while od[1] > 0:
                    if not tmp or od[0] < tmp[-1]:
                        buydic[od[0]] = buydic.setdefault(od[0], 0) + od[1]
                        break
                    tmpkey= tmp.pop()
                    if od[1] >= selldic[tmpkey]:
                        od[1] -= selldic[tmpkey]
                        del selldic[tmpkey]
                    else:
                        selldic[tmpkey] -= od[1]
                        break       
            elif od[2] == 1:
                tmp = sorted(buydic.keys())
                while od[1] > 0:
                    if not tmp or od[0] > tmp[-1]:
                        selldic[od[0]] = selldic.setdefault(od[0], 0) + od[1]
                        break
                    tmpkey= tmp.pop()
                    if od[1] >= buydic[tmpkey]:
                        od[1] -= buydic[tmpkey]
                        del buydic[tmpkey]
                    else:
                        buydic[tmpkey] -= od[1]
                        break
        res = 0
        for v in buydic.values() + selldic.values():
            res += v
        return res % (10**9+7)
    
"""
https://leetcode-cn.com/submissions/detail/157828172/

65 / 69 个通过测试用例
状态：超出时间限制
"""
