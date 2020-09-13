class Solution(object):
    def unhappyFriends(self, n, preferences, pairs):
        """
        :type n: int
        :type preferences: List[List[int]]
        :type pairs: List[List[int]]
        :rtype: int
        """
        
        length = len(pairs)
        dic = dict()
        for i in range(length):
            dic[pairs[i][0]] = i
            dic[pairs[i][1]] = i
        
        happy, unhappy = [], []
        
        def deal_with_pair(pair):
            for ind in [0,1]:
                if pair[ind] in happy or pair[ind] in unhappy:
                    continue
                tmplist = preferences[pair[ind]]
                pos = tmplist.index(pair[1-ind])
                for peopleInd in range(pos):
                    people = tmplist[peopleInd]
                    anotherPair = pairs[dic[people]]
                    anotherPeople = anotherPair[0] if people != anotherPair[0] else anotherPair[1]
                    anotherList = preferences[people]
                    pos2 = anotherList.index(anotherPeople)
                    pos3 = anotherList.index(pair[ind])
                    if pos2 > pos3:
                        if pair[ind] not in unhappy:
                            unhappy.append(pair[ind])
                        if people not in unhappy:
                            unhappy.append(people)
        
        for pair in pairs:
            deal_with_pair(pair)
        return len(unhappy)
    
"""
https://leetcode-cn.com/submissions/detail/107523794/

99 / 99 个通过测试用例
状态：通过
执行用时: 80 ms
内存消耗: 19.8 MB
"""
