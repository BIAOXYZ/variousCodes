class Solution(object):
    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        
        def is_power_of_two(num):
            while num > 2 and num % 2 == 0:
                num = num / 2
            if num == 2:
                return True
            return False
        
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
        keys = dic.keys()
        for i in range(len(keys)):
            if is_power_of_two(keys[i] + keys[i]) and dic[keys[i]] > 1:
                res += dic[keys[i]] * (dic[keys[i]] - 1) / 2
            for j in range(i+1, len(keys)):
                if is_power_of_two(keys[i] + keys[j]):
                    res += dic[keys[i]] * dic[keys[j]]
        return res % (10**9 + 7)
    
"""
https://leetcode-cn.com/submissions/detail/135548283/

4 / 72 个通过测试用例
状态：解答错误

输入：
[149,107,1,63,0,1,6867,1325,5611,2581,39,89,46,18,12,20,22,234]
输出：
10
预期：
12
"""
