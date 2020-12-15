
`738. 单调递增的数字` https://leetcode-cn.com/problems/monotone-increasing-digits/solution/dan-diao-di-zeng-de-shu-zi-by-leetcode-s-5908/
- [x] 方法一：贪心

# 测试用例

```
10
1234
332
56633
56733
45387
```
```
# 输出

9
1234
299
55999
56699
44999
```

# `000738.py`

算法的主要思想就是首先（从左向右，或者说从高位到低位）找到第一个比前一位小的数字`i`。然后从`i`开始往后面的都直接变成`9`；往前面的要看情况
