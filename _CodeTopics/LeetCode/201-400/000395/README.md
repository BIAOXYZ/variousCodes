
`395. 至少有K个重复字符的最长子串` https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters/solution/zhi-shao-you-kge-zhong-fu-zi-fu-de-zui-c-o6ww/
- [x] 方法一：分治
- [x] 方法二：滑动窗口

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
