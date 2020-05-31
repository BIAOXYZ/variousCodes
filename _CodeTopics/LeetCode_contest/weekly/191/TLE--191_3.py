class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        
        reachablelist = [0]
        changenum = 0
        tmpdic = {}
        
        def getKey(dic, val):
            return [k for k, v in dic.items() if v == val]
        
        def updateListAndDic(l, d):
            elem = l[-1]
            if d.has_key(elem):
                changenum += 1
                v = d[elem]
                l.append(v)
                del d[elem]
                updateListAndDic(l, d)
            elif elem in d.values():
                key = getKey(elem)
                l.append(key)
                del d[key]
                updateListAndDic(l, d)
            else:
                return
          
        for i in range(len(connections)):
            if connections[i][0] not in reachablelist and connections[i][1] in reachablelist:
                reachablelist.append(connections[i][0])
                updateListAndDic(reachablelist, tmpdic)
            elif connections[i][0] in reachablelist and connections[i][1] not in reachablelist:
                connections[i][0],connections[i][1] = connections[i][1],connections[i][0]
                changenum += 1
                reachablelist.append(connections[i][0])
                updateListAndDic(reachablelist, tmpdic)
            # 其实这个分支是不可能出现的，因为边的数量就n-1。不可能有两个节点都已经在reachablelist了，
            # 结果又出现了直接连接这两个节点的边，这样会形成环。
            elif connections[i][0] in reachablelist and connections[i][1] in reachablelist:
                continue
            else:
                tmpdic[connections[i][0]] = connections[i][1]
        return changenum
    
"""
# https://leetcode-cn.com/submissions/detail/75136150/

67 / 69 个通过测试用例
	状态：超出时间限制
最后执行的输入： 44667
                [[1,0],[2,1],[2,3],[4,0],[1,5],[6,2],[7,1],[6,8],[9,6],[7,10],[11,10],[2,12],[8,13],[14,1],[15,4],[16,2],[17,15],...
"""
