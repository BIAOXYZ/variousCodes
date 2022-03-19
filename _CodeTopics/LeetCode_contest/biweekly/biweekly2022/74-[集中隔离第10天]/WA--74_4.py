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
        while numCarpets > 0 and ind_len:
            curr = heapq.heappop(ind_len)
            if -curr[0] > carpetLen:
                heapq.heappush(ind_len, [curr[0]+carpetLen, curr[1]+carpetLen])
                res -= carpetLen
            else:
                res += curr[0]
            numCarpets -= 1
        return res
    
"""
https://leetcode-cn.com/submissions/detail/286088295/

2695 / 2698 个通过测试用例
状态：解答错误

输入：
"0001100111110001111111110111010110100111000111111001011011010000011011101100001011111111111111111011110101111011010101001011111111111111111011110101000101010010101111111011011111111101100111111101101111000011101101001110011011100010100111111111111111101011001111101110101110111001111111111110110111111101011110111000111011011010111011111111111111111011111011011111111110001110001100111001101101011111111111111111101011011111101101100111111111111111"
8
16
输出：
205
预期：
199
"""
"""
郁闷，就只差三个用例没过了！不是没鼠标 + 开始的晚，本地能调试下可能就过了。
"""
