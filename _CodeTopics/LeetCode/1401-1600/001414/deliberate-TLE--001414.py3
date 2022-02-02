class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:

        # 第一反应是算出来合适的斐波那契数列，然后reverse一下开始回溯，
        # 但这种算法是会超时的，不过还是写一下好了。
        # 写完后试了试：75025 还能过，121393 就超时了。

        fibonacciList = [1, 1]
        while fibonacciList[-1] < 10**9:
            fibonacciList.append(fibonacciList[-1] + fibonacciList[-2])
        ## print(fibonacciList)
        ## [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170]
        if fibonacciList[-1] > 10**9:
            fibonacciList.pop()
        
        revFib = list(reversed(fibonacciList))
        n = len(revFib)
        res = [n]
        def backtrack(pos, currInd, currSum):
            if currSum > k:
                return
            if currSum == k:
                res[0] = min(res[0], len(currInd)) 
                return
            for ind in range(pos, n):
                currInd.append(ind)
                currSum += revFib[ind]
                backtrack(ind+1, currInd, currSum)
                currSum -= revFib[ind]
                currInd.pop()
        
        backtrack(0, [], 0)
        return res[0]
        
"""
https://leetcode-cn.com/submissions/detail/264370445/

23 / 504 个通过测试用例
状态：超出时间限制

最后执行的输入：
513314
"""
