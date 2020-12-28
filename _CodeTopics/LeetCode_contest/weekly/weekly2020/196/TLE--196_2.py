class Solution(object):
    def getLastMoment(self, n, left, right):
        """
        :type n: int
        :type left: List[int]
        :type right: List[int]
        :rtype: int
        """
        
        def check(increment):
            for elem in increment:
                if elem == 0:
                    continue
                else:
                    return False
            return True
        
        pos = left + right
        length = len(pos)
        
        increment = []
        for i in range(len(left)):
            increment.append(-0.5)
        for i in range(len(right)):
            increment.append(0.5)
        for i in range(length):
            if (pos[i] == 0 and increment[i] == -0.5) or (pos[i] == n and increment[i] == 0.5):
                increment[i] = 0
        
        t = 0
        while not check(increment):
            t += 1
            ##print "Round ", t
            pos = [pos[i] + increment[i] for i in range(length)]
            ##print pos
            for i in range(length):
                if pos[i] == 0 or pos[i] == n:
                    increment[i] = 0
                if i < length -1 and pos[i] == pos[i+1]:
                    increment[i], increment[i+1] = -increment[i], -increment[i+1]
            ##print increment
        return t/2
    
"""
https://leetcode-cn.com/submissions/detail/84832255/

138 / 167 个通过测试用例
	状态：超出时间限制
"""
