
# 前言

参见[第 284 场周赛的笔记](https://github.com/BIAOXYZ/variousCodes/blob/master/_CodeTopics/LeetCode_contest/weekly/weekly2022/284-%5B%E9%9B%86%E4%B8%AD%E9%9A%94%E7%A6%BB%E7%AC%AC4%E5%A4%A9%5D/README.md)

从`3月9号`算起，那么今天是集中隔离的`第18天`。

# 中国时间：2022-03-27 10:30

第 286 场周赛 https://leetcode-cn.com/contest/weekly-contest-286
- 5268. 找出两数组的不同 https://leetcode-cn.com/contest/weekly-contest-286/problems/find-the-difference-of-two-arrays/
- 5236. 美化数组的最少删除数 https://leetcode-cn.com/contest/weekly-contest-286/problems/minimum-deletions-to-make-array-beautiful/
- 5253. 找到指定长度的回文数 https://leetcode-cn.com/contest/weekly-contest-286/problems/find-palindrome-with-fixed-length/
- 5269. 从栈中取出 K 个硬币的最大面值和 https://leetcode-cn.com/contest/weekly-contest-286/problems/maximum-value-of-k-coins-from-piles/

# 其他

今天临时听了 Hong Cheng 的一个报告，关于他们最新发表在 USENIX Security 2022 的工作 —— Cheetah: Lean and Fast Secure Two-Party Deep Neural Network Inference https://eprint.iacr.org/2022/207.pdf —— 所以基本是11:10之后才算去比赛，写了两道题，第三题看着有些类似之前没写出来的一道 Hard，于是不写了，歇一会，感觉好累。

# 其他2

这次周赛有个八卦，有个codeforces排名第三的[选手](https://codeforces.com/profile/jiangly)来参加周赛了。比国服第二名快了近三分钟，比全球第二也快了近一分钟。
- https://leetcode-cn.com/circle/discuss/LRecna/view/kIFe8n/
  * > jiangly大佬大驾降临lc，这lc周赛是越来越卷了……

# (3)

第三题`回文数`类型的题目有个技巧，以前没见过，这次学习到了算是：

https://leetcode-cn.com/circle/discuss/LRecna/view/cs0yN3/
```
第三题
这题属于关于回文数的问题，相信有做过类似关于回文数问题的 peers 都应该很熟悉如何处理。
只需查看整个长度的前一半的数字，并保持其依次增加即可（如 101, 111, 121 我们可以只看前面
的 10, 11, 12；1001, 1111, 1221 我们可以只看前面的 10, 11, 12）
由此可以简化为查找第 k 个 n+1 位数的问题，因此只要在 k<=9 * 10^n 的范围内找到对应的 n+1 位
数并在其后进行回文化处理即可；否则输出 -1 ，具体代码如下——
```
```py
class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        if intLength % 2:
            x = intLength // 2
            startNum = 10 ** x
            lst = []
            for query in queries:
                if query <= 9 * startNum:
                    string = str(startNum+query-1)
                    lst.append(int(string + string[-2::-1]))
                else:
                    lst.append(-1)
            return lst
        else:
            x = intLength // 2 - 1
            startNum = 10 ** x
            lst = []
            for query in queries:
                if query <= 9 * startNum:
                    string = str(startNum+query-1)
                    lst.append(int(string + string[::-1]))
                else:
                    lst.append(-1)
            return lst
```

# (4)

第四题在 Hard 里算相对简单的 dp 了，但是根本没看题，没办法。

https://leetcode-cn.com/circle/discuss/LRecna/view/vFeRjA/
