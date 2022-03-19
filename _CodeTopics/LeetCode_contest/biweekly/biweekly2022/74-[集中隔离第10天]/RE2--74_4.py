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
        if floor.count('1') == 0:
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
https://leetcode-cn.com/submissions/detail/286086897/

37 / 2698 个通过测试用例
状态：执行出错

执行出错信息：
IndexError: index out of range
    curr = heapq.heappop(ind_len)
Line 40 in minimumWhiteTiles (Solution.py)
    ret = Solution().minimumWhiteTiles(param_1, param_2, param_3)
Line 79 in _driver (Solution.py)
    _driver()
Line 89 in <module> (Solution.py)
最后执行的输入：
"001111110000000011111111010011110100001111000000000111111110000110000000000000001010111111111011110011111111000000010011110000111101111000111101111000111101100111100111100001111001111010000000000000000000100000100000000111100000000001100011111111011111000011111100001000000001111001111111111111011110100001111111101111101111000011110011110001111001111011111111000111100111111111111111100001111000"
68
4
"""
