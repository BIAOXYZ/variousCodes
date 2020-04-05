
# 2020.04.05

第 183 场周赛 https://leetcode-cn.com/contest/weekly-contest-183
- 5376. 非递增顺序的最小子序列 https://leetcode-cn.com/contest/weekly-contest-183/problems/minimum-subsequence-in-non-increasing-order/
- 5377. 将二进制表示减到 1 的步骤数 https://leetcode-cn.com/contest/weekly-contest-183/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/
- 5195. 最长快乐字符串 https://leetcode-cn.com/contest/weekly-contest-183/problems/longest-happy-string/
- 5379. 石子游戏 III https://leetcode-cn.com/contest/weekly-contest-183/problems/stone-game-iii/

# 笔记

## (2) 

>> notes：MLGB，第二题第一种方法转成整数去做超时我就不说啥了，第二种就是字符串凭啥超时，而且一个用例都没过？我本地全踏马运行的好好的！

```
1011 11
----------
1100 12
110 6
11 3
100 4
10 2
1 1

1101 13
----------
1110 14
111 7
1000 8
100 4
10 2
1 1

xxxxx0111 到 xxxxx1，其实可以通过判断只要倒数第二位不是0，就一直走。
直到倒数第二位为0的那位，有几个1就是几步，然后那个0变成1。
----------
xxxxx1000
xxxxx100
xxxxx10
xxxxx1
```
