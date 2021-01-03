class Solution(object):
    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        
        def list_to_dict(lis):
            dic = {}
            for num in lis:
                if dic.has_key(num):
                    dic[num] += 1
                else:
                    dic[num] = 1
            return dic
        
        dic = list_to_dict(deliciousness)
        res = 0
        res2 = 0
        keys = dic.keys()
        
        for num in keys:
            for i in range(22):
                if dic.has_key(2**i - num) and 2**i - num == num:
                    res2 += dic[num] * (dic[num] - 1) / 2
                    break
            for i in range(22):
                if dic.has_key(2**i - num) and 2**i - num != num:
                    res += dic[num] * dic[2**i - num]
        res /= 2
        res += res2
        return res % (10**9 + 7)
    
"""
https://leetcode-cn.com/submissions/detail/135559985/

69 / 72 个通过测试用例
状态：通过
执行用时: 952 ms
内存消耗: 21.2 MB
"""
"""
注：我也一脸懵逼，这是什么鬼？。。。如果经过了一段时间后，当时通过的用例数比总用例数少也正常，因为会不断添加。但是这才刚做完题不到一小时。。。
"""
