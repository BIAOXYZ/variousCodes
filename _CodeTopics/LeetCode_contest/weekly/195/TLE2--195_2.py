class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        
        # [-1%3, -5%3] = [2,1]
        # 所以可以先全转成不超过k的数。
        
        length = len(arr)
        for i in range(length):
            arr[i] = arr[i] % k

        if arr.count(0) % 2 != 0:
            return False
        
        for i in range(1,k/2):
            if arr.count(i) != arr.count(k-i):
                return False
        return True
    
"""
https://leetcode-cn.com/submissions/detail/82635210/

86 / 91 个通过测试用例
	状态：超出时间限制
"""
