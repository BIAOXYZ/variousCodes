class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        dic = {}
        for ch in tasks:
            if dic.has_key(ch):
                dic[ch] += 1
            else:
                dic[ch] = 1
        maxFreq = max(dic.values())
        
        keyList = dic.keys()
        keyList.sort(key=lambda k:dic[k], reverse=True)
        sortedLoopList = [[k]*dic[k] for k in keyList]
        """
        sortedLoopList = []
        for k in keyList:
            for freq in range(dic[k]):
                sortedLoopList.append(k)
        
        对于 ["A","A","A","B","B","B","B"]，这段代码的结果是：
        ["B","B","B","B","A","A","A"]。
        """

        res = []
        index = 0
        while sortedLoopList:
            tmp = []
            for i in range(n+1):
                if sortedLoopList[index][0] not in tmp:
                    tmp.append(sortedLoopList[index].pop())
                    if not sortedLoopList[index]:
                        sortedLoopList.pop(index)
                        if not sortedLoopList:
                            break
                        index = index % len(sortedLoopList)
                    else:    
                        index = (index + 1) % len(sortedLoopList)
                else:
                    tmp.append('placeholder')
            res += tmp[:]
        print res
        return len(res)
        
"""
https://leetcode-cn.com/submissions/detail/128856411/

30 / 71 个通过测试用例
状态：解答错误

输入：
["A","A","A","A","A","A","B","C","D","E","F","G"]
2
输出：
19
预期：
16
"""
