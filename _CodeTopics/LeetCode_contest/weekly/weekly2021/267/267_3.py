class Solution(object):
    def decodeCiphertext(self, encodedText, rows):
        """
        :type encodedText: str
        :type rows: int
        :rtype: str
        """
        
        if not encodedText:
            return ''
        if rows == 1:
            return encodedText
        length = len(encodedText)
        cols = length / rows
        
        mtx = []
        for i in range(0, length, cols):
            tmp = list(encodedText[i:i+cols])
            mtx.append(tmp)
        
        res = ''
        for start_ind_of_first_row in range(cols):
            res += mtx[0][start_ind_of_first_row]
            is_end = False
            for i in range(1, rows):
                newrow = 0 + i
                newcol = start_ind_of_first_row + i
                if newrow < rows and newcol < cols:
                    res += mtx[newrow][newcol]
                else:
                    is_end = True
                    break
            if is_end:
                break
        return res.rstrip()
    
"""
https://leetcode-cn.com/submissions/detail/238453602/

39 / 39 个通过测试用例
状态：通过
执行用时: 108 ms
内存消耗: 30 MB
"""
