class Solution(object):
    def minimumWhiteTiles(self, floor, numCarpets, carpetLen):
        """
        :type floor: str
        :type numCarpets: int
        :type carpetLen: int
        :rtype: int
        """
        
        n = len(floor)
        if numCarpets * carpetLen >= n:
            return 0
        
        ind_len = []
        flag = 0
        tmplen = 0
        i = 0
        while i < n:
            if floor[i] == '0':
                flag = 0
                if tmplen > 0:
                    ind_len.append([-tmplen, i-tmplen])
                    tmplen = 0
            elif floor[i] == '1':
                if flag == 0:
                    flag = 1
                    tmplen = 1
                else:
                    tmplen += 1
            i += 1
        if tmplen > 0:
            ind_len.append([-tmplen, n-tmplen])
        ## print(ind_len)
        
        heapq.heapify(ind_len)
        res = floor.count('1')
        while numCarpets > 0:
            curr = heapq.heappop(ind_len)
            if -curr[0] > carpetLen:
                heapq.heappush(ind_len, [curr[0]+carpetLen, curr[1]+carpetLen])
                res -= carpetLen
            else:
                res += curr[0]
            numCarpets -= 1
        return res
    
"""
https://leetcode-cn.com/submissions/detail/286085268/

2 / 2698 个通过测试用例
状态：执行出错

执行出错信息：
IndexError: index out of range
    curr = heapq.heappop(ind_len)
Line 38 in minimumWhiteTiles (Solution.py)
    ret = Solution().minimumWhiteTiles(param_1, param_2, param_3)
Line 77 in _driver (Solution.py)
    _driver()
Line 87 in <module> (Solution.py)
最后执行的输入：
"0000"
1
1
"""
