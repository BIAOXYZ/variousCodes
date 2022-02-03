class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:

        # 参考官方答案思想的版本：纯数学分析后，只是贪心地取当前斐波那契数列里最大那个即可。
        fibonacciList = [1, 1]
        while fibonacciList[-1] < k:
            fibonacciList.append(fibonacciList[-1] + fibonacciList[-2])
        
        ind = len(fibonacciList) - 1
        res = 0
        while k > 0:
            while fibonacciList[ind] > k:
                ind -= 1
            k -= fibonacciList[ind]
            res += 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/264461894/

执行用时：44 ms, 在所有 Python3 提交中击败了27.03%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了32.43%的用户
通过测试用例：
504 / 504
"""
