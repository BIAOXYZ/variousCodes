class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """

        def traverse_hour(n):
            if n == 0: return ['0']
            elif n == 1: return ['1','2','4','8']
            # elif n == 2: return ['3','5','9','6','10','12']
            elif n == 2: return ['3','5','9','6','10']
            # elif n == 3: return ['14','13','11','7']
            elif n == 3: return ['11','7']
            # else: return ['15']
            else: return []
        def traverse_minute(n):
            if n == 0: return ['00']
            elif n == 1: return ['01','02','04','08','16','32']
            elif n == 2: return ['03','05','09','17','33','06','10','18','34','12','20','36','24','40','48']
            elif n == 3: return ['07','11','19','35', '13','21','37', '25','41', '49',   '14','22','38', '26','42', '50',   '28','44', '52',   '56']
            # 63 - 03 = 60，舍弃。
            elif n == 4: return ['58','54','46','30','57','53','45','29','51','43','27','39','23','15']
            # 63 - 01，63 - 02 均舍弃。
            elif n == 5: return ['59','55','47','31']
            else: return []

        res = []
        h, m = [], []
        for hourBits in range(min(5, turnedOn+1)):
            minuteBits = turnedOn - hourBits
            h = traverse_hour(hourBits)
            m = traverse_minute(minuteBits)
            if h and m:
                for s1 in h:
                    for s2 in m:
                        res.append(s1 + ':' + s2)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/188335878/

10 / 10 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.2 MB

执行用时：20 ms, 在所有 Python 提交中击败了61.33%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了8.00%的用户
"""
