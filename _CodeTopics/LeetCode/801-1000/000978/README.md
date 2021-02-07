
`978. 最长湍流子数组` https://leetcode-cn.com/problems/longest-turbulent-subarray/solution/zui-chang-tuan-liu-zi-shu-zu-by-leetcode-t4d8/
- [x] 方法一：双指针
- 方法二：动态规划

🎦 最长湍流子数组 https://leetcode-cn.com/problems/longest-turbulent-subarray/solution/zui-chang-tuan-liu-zi-shu-zu-by-leetcode-zqoq/
- 方法一：动态规划
- 方法二：双指针

# 测试用例

```
[9,4,2,10,7,8,8,1,9]
[4,8,12,16]
[100]
[0,1,1,0,1,0,1,1,0,0]
[0,8,45,88,48,68,28,55,17,24]
[4,5]
```

# `WA--000978.py`、`WA2--000978.py`、`WA3--000978.py`

- `WA--000978.py`：纯属手误，把真正的数组都给写错了，应该是后面的四处`arr`其实都是`tmplis`。
- `WA2--000978.py`：滑动窗口类型题常见错误，遍历完成后最后的那个可能也符合，但是没有计入。
- `WA3--000978.py`：这里就只是`arr`里有2个元素的corner case了，其实可以在开头直接根据length简单的返回一些值，但是不是很想那么做。所以硬是又改了下，到`000978.py`才算改对。不过整体代码都挺丑陋的。
