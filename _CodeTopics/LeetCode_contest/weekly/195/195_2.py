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

        # 如果0的数目不是偶数个，肯定不对。
        if arr.count(0) % 2 != 0:
            return False    
        
        # 用lambda表达式删除所有0，如果用remove只能一次移除一个0。
        arr = filter(lambda x: x != 0, arr)
        arr.sort()
        
        newlength = len(arr)
        for i in range(newlength/2):
            if arr[i] + arr[newlength-1-i] != k:
                return False
        return True
    
"""
https://leetcode-cn.com/submissions/detail/82639935/

91 / 91 个通过测试用例
	状态：通过
执行用时：172 ms
内存消耗：21 MB
"""
