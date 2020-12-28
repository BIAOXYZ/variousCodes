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
        ##print arr
        while arr != []:
            # 这里是防止 temp = k - 0 等于 k，然后查找k时已经不在数组里了。
            temp = (k - arr[0]) % k
            ##print "temp = ", temp
            ##print arr.index(temp,1)
            # 这里是让查找index至少从1开始。
            if temp in arr and temp != arr[0]:
                arr.remove(temp)
                arr.remove(arr[0])
            elif temp in arr and temp == arr[0]:
                if arr.count(temp) <= 1:
                    return False
                else:
                    arr.remove(arr[0])
                    arr.remove(temp)
            else:
                return False
            ##print arr
        return True
    
"""
https://leetcode-cn.com/submissions/detail/82632048/

86 / 91 个通过测试用例
	状态：超出时间限制
  
# 最后超时用例不贴了。
"""
