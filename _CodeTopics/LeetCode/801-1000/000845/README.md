
`845. 数组中的最长山脉` https://leetcode-cn.com/problems/longest-mountain-in-array/solution/shu-zu-zhong-de-zui-chang-shan-mai-by-leetcode-sol/
- [x] 方法一：枚举山顶 【实质上是动态规划】
- [x] 方法二：枚举山脚 【实质上是双指针】

# 测试用例

```
[2,1,4,7,3,2,5]
[2,2,2]
[1,2,3,4]
[]
[0,1,2,3,4,5,4,3,2,1,0]
```

# `000845_algo3.py`

这个对应官方第二种，即双指针解法。说实话官方的实现还是不太好的：因为左半边山峰（也就是上升段）在官方代码里也成了right指针在移动——当然，可以认为官方答案的想法是左指针left固定后，一直是右指针在移动——但是我还是觉得记录一下left的初始位置（originalLeft），然后左半段左指针移动，右半段右指针移动比较好。
