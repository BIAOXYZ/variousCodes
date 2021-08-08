
`313. 超级丑数` https://leetcode-cn.com/problems/super-ugly-number/solution/chao-ji-chou-shu-by-leetcode-solution-uzff/
- [x] 方法一：最小堆
- [ ] 方法二：动态规划

# 测试用例

```
12
[2,7,13,19]
1
[2,3,5]
```

# TODO

// 有点类似dp，但是没写完，回头想补就补一下吧。
```py
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """

        """
        # primes = [2,3,5] 时，前面的一些数是这样的：
        # ugly_nums = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 27, 30, 32]
        # 我们不妨假定当前最大的是12，求下一个数可以这样计算：
        ## 12 * 2 = 24，但这不一定紧接着的大于 12 的那个数，不过像 12*3，12*5 就更不用考虑了。需要考虑的是这些：
        ## 12 * (3 / 2.0) = 18, 12 * (4 / 3.0) = 16, 12 * (5 / 3.0) = 20, 12 * (5 / 4.0) = 15。
        ## 然后可求得最小的就是 min(24, 18, 16, 20, 15) = 15。
        """

        if n == 1:
            return 1
        
        length = len(primes)
        currPrimeComponent = [1] + [0 for _ in range(length-1)]
        currNum = primes[0]
        while n - 2 > 0:
            n -= 1
            for i in range(length):
                for j in range(currPrimeComponent[i]):
              
```
