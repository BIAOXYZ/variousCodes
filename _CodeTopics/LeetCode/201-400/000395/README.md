
`395. 至少有K个重复字符的最长子串` https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters/solution/zhi-shao-you-kge-zhong-fu-zi-fu-de-zui-c-o6ww/
- [x] 方法一：分治
- [x] 方法二：滑动窗口

【相信科学系列】为什么不能用「滑动窗口」？以及如何发掘题目性质 ... https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters/solution/xiang-jie-mei-ju-shuang-zhi-zhen-jie-fa-50ri1/

# 测试用例

```
"aaabb"
3
"ababbc"
2
"xyzyyx"
2
"xyzyyy"
2
"xyzww"
2
"ababacb"
3
"bbaaacbd"
3
"bbaaacddcaabdbd"
3
```

# `WA3--000395.py`

这个基本已经接近正确实现`000395.py`了，就是递归调用那行（第28行）粗心了。

# `000395.py`

这个其实核心还是分治+递归，因为虽然用到了滑动窗口，但是有些情况纯滑动窗口处理不了，结果还得递归调用。

# `000395_algo2.py`

纯滑动窗口实现，在该实现中需要额外引入“**当前窗口中总的字母种类**”这个变量，有了这个变量，滑动窗口才有了“二段性”。参考： https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters/solution/xiang-jie-mei-ju-shuang-zhi-zhen-jie-fa-50ri1/

实际上这个实现有Hard的难度了吧。。。

# `000395_algo3.py`

纯分治 + 递归实现。反而是三种里面最好写的。。。另外我感觉我的实现好像比答案的简单不少（虽然也没细看答案，粗看下感觉应该是的）。
