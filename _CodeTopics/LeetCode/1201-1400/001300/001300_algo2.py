class Solution(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        
        length = len(arr)
        arr.sort()
        sumCache = [0]
        for i in range(length):
            sumCache.append(sumCache[-1] + arr[i])
        
        # 寻找某个中间位置的值（注意是值），使得变化后的总和小于等于且最接近target
        left, right = 0, max(arr)
        # 官方答案这个赋值了-1，我感觉max(arr)才更对吧
        resAns = max(arr)
        # 这里必须有等号，不然会有问题，可以试试打开代码里的print，看下输入为
        # arr = [4,9,3], target = 10
        # 时的标准输出就明白了。
        while left <= right:
            mid = (left + right) / 2
            pos = bisect.bisect_left(arr, mid)
            currSum = sumCache[pos] + (length - pos) * mid
            ##print "left is: ", left
            ##print "right is: ", right
            ##print "mid is: ", mid
            if currSum <= target:
                resAns = mid
                left = mid + 1
            else:
                right = mid - 1
            ##print resAns

        pos = bisect.bisect_left(arr, resAns)
        abssmall = abs(sumCache[pos] + (length - pos) * resAns - target)
        pos2 = bisect.bisect_left(arr, resAns+1)
        absbig = abs(sumCache[pos2] + (length - pos2) * (resAns+1) - target)
        if abssmall <= absbig:
            return resAns
        else:
            return resAns+1
            
"""
https://leetcode-cn.com/submissions/detail/80106898/

18 / 18 个通过测试用例
状态：通过
执行用时：24 ms
内存消耗：13.6 MB
"""
"""
执行结果：通过
显示详情
执行用时 :24 ms, 在所有 Python 提交中击败了97.49%的用户
内存消耗 :13.6 MB, 在所有 Python 提交中击败了100.00%的用户
"""
