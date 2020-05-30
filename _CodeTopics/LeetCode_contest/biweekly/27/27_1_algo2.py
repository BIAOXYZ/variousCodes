class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        
        # 其实只要两个数组元素一样就总能翻转到一模一样。。。方法就是类似冒泡排序那样两两交换
        # 题目提示里已经有 target.length == arr.length，故不再判断
        """
        def isIn(num, numarr):
            for i in range(len(numarr)):
                if num == numarr[i]:
                    return True
            return False
        
        length = len(arr)
        for i in range(length):
            if isIn(arr[i], target) == False:
                return False
        return True
        """
        
        # 上面那段代码还没提交就自己发现问题了，[1,1,1,1,2]和[1,1,1,2,2]也会返回True，其实应该是False。
        # 也就是说，不光元素都得有，元素个数还必须一样。
        def isIn(num, numarr):
            for i in range(len(numarr)):
                if num == numarr[i]:
                    return True
            return False
        def updateDic(k, d):
            if d.has_key(k):
                d[k] += 1
            else:
                d[k] = 1
        
        length = len(arr)
        # 这里最早图省事写的是： dic_a = dic_t = {}
        # 结果发现这样写等于是一个字典。。。
        dic_a = {}
        dic_t = {}
        for i in range(length):
            if isIn(arr[i], target) == False or isIn(target[i], arr) == False:
                return False
            else:
                updateDic(arr[i], dic_a)
                updateDic(target[i], dic_t)
        res = cmp(dic_a, dic_t)
        if res == 0:
            return True
        else:
            return False
    
"""
# https://leetcode-cn.com/submissions/detail/75013850/

99 / 99 个通过测试用例
	状态：通过
执行用时：216 ms
内存消耗：12.9 MB
"""
