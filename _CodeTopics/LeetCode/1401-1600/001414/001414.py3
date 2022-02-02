class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:

        # 其实用回溯也不是不行，只是需要些特殊处理：
        #   因为有贪心策略在，所以一旦发现了结果，一定是最优结果。
        #   此时也不用再管什么状态的还原了，直接一路 return True 回去，直到最外层。
        
        # 此外，由于用的是 Python3，不需要再跟 Python2 一样把 res 搞成个list了，
        #   直接在函数里用 nonlocal res 先声明下，就可以一层层直接用了。

        fibonacciList = [1, 1]
        while fibonacciList[-1] < 10**9:
            fibonacciList.append(fibonacciList[-1] + fibonacciList[-2])
        ## print(fibonacciList)
        ## [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170]
        if fibonacciList[-1] > 10**9:
            fibonacciList.pop()
        
        revFib = list(reversed(fibonacciList))
        n = len(revFib)
        res = n
        def backtrack(pos, currInd, currSum):
            resultFound = False
            if currSum > k:
                return resultFound
            if currSum == k:
                nonlocal res
                res = min(res, len(currInd)) 
                return not resultFound
            for ind in range(pos, n):
                currInd.append(ind)
                currSum += revFib[ind]
                subResult = backtrack(ind+1, currInd, currSum)
                if subResult:
                    return subResult
                currSum -= revFib[ind]
                currInd.pop()
        
        backtrack(0, [], 0)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/264376542/

执行用时：44 ms, 在所有 Python3 提交中击败了27.03%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了9.46%的用户
通过测试用例：
504 / 504
"""
