
class Solution(object):
    def conveyorBelt(self, matrix, start, end):
        """
        :type matrix: List[str]
        :type start: List[int]
        :type end: List[int]
        :rtype: int
        """
        
        # 以end为起点进行BFS，按需要多少次改变分层？
        
        m, n = len(matrix), len(matrix[0])
        dic = {'^':(-1,0), 'v':(1,0), '<':(0,-1), '>':(0,1)}
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        def is_legal(coor):
            x, y = coor
            return 0 <= x < m and 0 <= y < n
        def can_direct_reach(coor1, coor2):
            x1, y1 = coor1
            x2, y2 = coor2
            return (x1-x2, y1-y2) == dic[matrix[x2][y2]]
        
        visited = set()
        results = {tuple(end):0}
        q = deque([end])
        while q:
            print '*'*50
            print q
            currLen = len(q)
            for i in range(currLen):
                curr = tuple(q.popleft())
                if curr in visited:
                    continue
                visited.add(curr)
                print curr, '||||', visited, '||||', results
                for d in directions:
                    nextNode = (curr[0] + d[0], curr[1] + d[1])
                    print "nextNode is: ", nextNode
                    if not is_legal(nextNode):
                        continue
                    q.append(nextNode)
                    if can_direct_reach(curr, nextNode):
                        results[nextNode] = min(results.get(nextNode, 201), results[curr])
                    else:
                        results[nextNode] = min(results.get(nextNode, 201), results[curr]+1)
                    print "results[nextNode]: ", results[nextNode], "resultes: ", results
        return results[tuple(start)]
    
