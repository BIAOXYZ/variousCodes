
`121. 买卖股票的最佳时机` https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/121-mai-mai-gu-piao-de-zui-jia-shi-ji-by-leetcode-/
- [x] 方法一：暴力法
- [x] 方法二：一次遍历  【其实算是不明显的动态规划吧】

股票问题（Python3、C++） https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/gu-piao-wen-ti-python3-c-by-z1m/
- > 股票问题一共有六道：买卖股票的最佳时机（1，2，3，4）、含冷冻期、含手续费。本题是第一道，属于入门题目。
- > 股票问题的方法就是 动态规划，因为它包含了重叠子问题，即买卖股票的最佳时机是由之前买或不买的状态决定的，而之前买或不买又由更早的状态决定的...由于本题只有一笔交易（买入卖出），因此除了动态规划，我们还可以使用更加简便的方法实现。
- > 思路（官方题解方法二：一次遍历）
- > 方法二：动态规划

# 测试用例

```
[7,1,5,3,6,4]
[7,6,4,3,1]
[1,2,3,4,5]
[1]
[1,2]
[2,1]
```

# `000121_algo3_impl.py`

注意看这个代码里面的注释，里面说明了为什么**两种一次遍历实现**（`000121_algo2.py`、`000121_algo2.py`）和**两种动态规划实现**（`000121_algo3.py`、`000121_algo3_impl.py`）在for循环里那两句的顺序可以交换，以及为什么**更新currMinPrice的那句**在后面才是更准确的。
