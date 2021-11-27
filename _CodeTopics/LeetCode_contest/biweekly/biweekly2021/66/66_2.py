class Solution(object):
    def minimumBuckets(self, street):
        """
        :type street: str
        :rtype: int
        """
        
        n = len(street)
        if all(street[i] == '.' for i in range(n)):
            return 0
        if street == 'H' or street.startswith('HH') or street.endswith('HH') or street.find('HHH') != -1:
            return -1
        
        street = list(street)
        i = 0
        res = 0
        while i < n:
            if street[i] in ['B', '.']:
                i += 1
                continue
            if street[i] == 'H':
                if (0 <= i-1 <= n-1 and street[i-1] == 'B') or (0 <= i+1 <= n-1 and street[i+1] == 'B'):
                    i += 1
                    continue
                if 0 <= i+1 <= n-1 and street[i+1] == '.':
                    street[i+1] = 'B'
                    res += 1
                elif 0 <= i-1 <= n-1 and street[i-1] == '.':
                    street[i-1] = 'B'
                    res += 1
                i += 1
        return res
    
"""
https://leetcode-cn.com/submissions/detail/242935706/

207 / 207 个通过测试用例
状态：通过
执行用时: 96 ms
内存消耗: 17.4 MB
"""
