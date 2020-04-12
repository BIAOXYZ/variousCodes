class Node:
    def __init__(self,value=None,nextnode=None):
        self.val = value
        self.next = nextnode
        self.position = 0

class Solution(object):
    def processQueries(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        
        def formListFromPosition(oldlist,position):
            if position == 0:
                return oldlist
            newlist = [oldlist[position]]
            for i in range(position):
                newlist.append(oldlist[i])
            for i in range(position+1,len(oldlist)):
                newlist.append(oldlist[i])
            return newlist
            
        
        p = range(1,m+1,1)
        res = []
        """
        startnode = currnode = Node(1)
        for value in range(2,m+1):
            newnode = Node(value)
            currnode.next = newnode
            currnode = newnode
        """  
        for i in range(len(queries)):
            position = p.index(queries[i])
            res.append(position)
            p = formListFromPosition(p,position)
        return res
        
