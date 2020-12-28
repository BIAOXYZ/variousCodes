class Solution(object):
    def canConvertString(self, s, t, k):
        """
        :type s: str
        :type t: str
        :type k: int
        :rtype: bool
        """
        
        # 核心思想就是算出来s到t需要的最小变换次数，然后和k比较大小即可。
        
        if len(s) != len(t):
            return False
        
        length = len(s)
        sub = {}
        for i in range(length):
            if t[i] == s[i]:
                continue
            tmp = ord(t[i]) - ord(s[i])
            if tmp < 0:
                tmp = 26 + tmp
            if not sub.has_key(tmp):
                sub[tmp] = 1
            else:
                sub[tmp] += 1
        
        min_change_time = 0
        for key, val in sub.items():
            min_change_time = max(min_change_time, (val-1)*26+key)
        
        return min_change_time <= k
    
"""
https://leetcode-cn.com/submissions/detail/96076661/

154 / 154 个通过测试用例
	状态：通过
执行用时：496 ms
内存消耗：17.5 MB
"""
