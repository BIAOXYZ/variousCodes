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
        print dic
        res = 0
        keys = dic.keys()
        usedKeys = set([])
        
        for num in keys:
            if num in usedKeys:
                for i in range(22):
                    if dic.has_key(2**i - num) and 2**i - num == num:
                        res += dic[num] * (dic[num] - 1) / 2
                continue
            for i in range(22):
                if dic.has_key(2**i - num):
                    if 2**i - num != num:
                        res += dic[num] * dic[2**i - num]
                    else:
                        res += dic[num] * (dic[num] - 1) / 2
                    usedKeys.add(2**i - num)
                    print num, 2**i - num
        return res % (10**9 + 7)
    
"""
https://leetcode-cn.com/submissions/detail/135557974/

14 / 72 个通过测试用例
状态：解答错误

输入：
[3741,355,2,0,2,2,333,179,46,18,919,105,10947,5437,3882,4310,94,162,13,3,1006,1042,3423,673,791,233,26,6,6,2,148,364,3,1,582,442,5676,2516,3525,571,0,2,9230,7154,421,603,1701,2395,122,134,653,7539,6717,1475,1,0,4,0,38,90,388,124,1,0,25551,7217,15,17,453,571,3,13,3,5,1,1,4,28,3543,4649,902,15482,0,2,10,6,3566,530,12926,3458,40,472,28,4,85,43,215,297,2,14,238,18,416,96,5,3,494,18,0,1,48,80,229,1819,0,2,0,1,26510,6258,2,6,1487,2609,6,10,1821,2275,1726,322,7,9,252,4,1,3,3,1,8,0,836,188,102,154,13,115,0,4,2,30,31,1,4,4,102,8090,101,155,5354,2838,1110,2986,1,3,2,2,4,4,203,1845,3,13,5,3]
输出：
979
预期：
947
"""
