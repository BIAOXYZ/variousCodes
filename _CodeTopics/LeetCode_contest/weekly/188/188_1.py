class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        
        """ 
        思路：某个数在target，就一次push；不在target，一次push+一次pop
        """
        
        resList = []
        
        difference1 = target[0] - 1
        """
        # 这里不能改变target数组里元素的值，否则有问题。
        # while target[0] - 1 > 0:
        # 比如[2,3]，第一轮完变成[1,3]了，后面的for循环就错了。
        """
        while difference1 > 0:
            resList.append("Push")
            resList.append("Pop")
            difference1 -= 1
        resList.append("Push")
        
        for i in range(1, len(target), 1):
            difference2 = target[i] - target[i-1]
            while difference2 > 1:
                resList.append("Push")
                resList.append("Pop")
                difference2 -= 1
            resList.append("Push")
        
        return resList
    
"""
这次为啥没有多少个用例过了之类的？坑爹系统。。。
"""
