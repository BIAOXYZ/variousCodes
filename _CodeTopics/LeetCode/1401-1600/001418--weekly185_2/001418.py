class Solution(object):
    def displayTable(self, orders):
        """
        :type orders: List[List[str]]
        :rtype: List[List[str]]
        """

        foods = set()
        tables = {}
        for order in orders:
            table, food = order[1], order[2]
            foods.add(food)
            if tables.has_key(table):
                tables[table][food] = tables[table].setdefault(food, 0) + 1
            else:
                tables[table] = {food:1}
        
        res = []
        foods = list(foods)
        foods.sort()
        res.append(['Table'] + foods)

        sortedTableNums = tables.keys()
        sortedTableNums.sort(key = lambda x : int(x))
        tmp = []
        for tableNum in sortedTableNums:
            tmp.append(str(tableNum))
            currTable = tables[tableNum]
            for food in foods:
                if currTable.has_key(food):
                    tmp.append(str(currTable[food]))
                else:
                    tmp.append(str(0))
            res.append(tmp[:])
            tmp = []
        return res
        
"""
https://leetcode-cn.com/submissions/detail/192702062/

53 / 53 个通过测试用例
状态：通过
执行用时: 384 ms
内存消耗: 22.1 MB

执行用时：384 ms, 在所有 Python 提交中击败了100.00%的用户
内存消耗：22.1 MB, 在所有 Python 提交中击败了40.00%的用户
"""
"""
这个超越百分之百时间是没想到的。。。感觉写的虽然不算多复杂，也不能算简洁啊。。。
"""
