class Solution(object):
    def minimumOperations(self, nums, start, goal):
        """
        :type nums: List[int]
        :type start: int
        :type goal: int
        :rtype: int
        """
        
        dic = {start:0}
        def memorize_search(currStart, currNumOfTimes):
            # if not dic.has_key(currStart):
            #     dic[currStart] = currNumOfTimes
            if currStart == goal:
                return
            if currStart < 0 or currStart > 1000:
                #dic[currStart] = float('inf')
                return
            for num in nums:
                flag1 = flag2 = flag3 = False
                if not dic.has_key(currStart - num):
                    dic[currStart - num] = currNumOfTimes + 1
                    flag1 = True
                if not dic.has_key(currStart + num):
                    dic[currStart + num] = currNumOfTimes + 1
                    flag2 = True
                if not dic.has_key(currStart ^ num):
                    dic[currStart ^ num] = currNumOfTimes + 1
                    flag3 = True
                if flag1:
                    memorize_search(currStart - num, currNumOfTimes + 1)
                if flag2:
                    memorize_search(currStart + num, currNumOfTimes + 1)
                if flag3:
                    memorize_search(currStart ^ num, currNumOfTimes + 1)
        
        memorize_search(start, 0)
        if dic.has_key(goal) and dic[goal] != float('inf'):
            return dic[goal]
        return -1
    
"""
https://leetcode-cn.com/submissions/detail/233996273/

28 / 51 个通过测试用例
状态：解答错误

最后执行的输入：
[3,5,7]
0
-4
"""
