class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        
        # 因为limit最小是0，所以不管怎么样单个元素形成的连续子数组也满足条件
        # 所以初始的最长连续子数组长度也是从1开始而不是从0开始
        # 我觉得题目描述不太好，根本不会有返回0的情况（条件里说了nums也不为空）
        maxSubArrayLen = 1
        length = len(nums)
        
        for i in range(length):
            for j in range(i+1,length):
                flag = True
                for k in range(i,j):
                    if abs(nums[j] - nums[k]) <= limit:
                        continue
                    else:
                        flag = False
                        break
                # 这里直接跳出第二层for循环。仔细看看想想就明白：
                # 在哪个for循环内部执行的逻辑里进行break，就跳出哪个for循环！
                # 所以上面那个break是跳出第三层for循环，而这个是跳出第二层for循环。
                if flag == False:
                    break
                if j - i + 1 > maxSubArrayLen:
                    maxSubArrayLen = j - i + 1
        return maxSubArrayLen
    
"""
52 / 54 个通过测试用例
	状态：超出时间限制
最后执行的输入： [7386080,9043369,566116,155607,2192513,5102709,8009203,8124311,9220099,588704,7572203,4133378,3288454,1209376,22421...
"""
