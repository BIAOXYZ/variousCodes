class Solution(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        
        summation = sum(arr)
        minisub = summation - target
        if minisub == 0:
            return max(arr)
        # 实际上根据题意这个分支应该不存在。
        if minisub < 0:
            return -1

        length = len(arr)
        arr.sort(reverse=True)
        ## 这里暂时想不到这个平均数该怎么用，不用吧肯定不对，比如例子里
        ## [60864,25176,27249,21296,20204]，下面while+for循环完也见不了多少。
        ## average = target / length

        this_round_pos = 0
        while minisub > 0:
            value = arr[this_round_pos] - 1
            minisub -= this_round_pos * 1
            for i in range(this_round_pos, length):
                if arr[i] <= value:
                    this_round_pos = i
                    break
                arr[i] = value
                minisub -= 1
        if minisub == 0:
            return arr[this_round_pos-1]
        if minisub < 0:
            if abs(minisub) < abs(minisub - this_round_pos):
                return arr[this_round_pos-1] + 1
            else:
                return arr[this_round_pos-1]
                
"""
https://leetcode-cn.com/submissions/detail/78976869/

2 / 18 个通过测试用例
状态：解答错误

输入：[60864,25176,27249,21296,20204]
      56803
输出：21296
预期：11361
"""
