
`521. 最长特殊序列 Ⅰ` https://leetcode-cn.com/problems/longest-uncommon-subsequence-i/solution/zui-chang-te-shu-xu-lie-i-by-leetcode-so-v9sr/
- [x] 方法一：脑筋急转弯

```
"aba"
"cdc"
"aaa"
"bbb"
"aaa"
"aaa"
```

# 语法点：单行的三重（甚至是多重）if表达式

翻译 python：能否把 if-elif-else写成一行的形式？ https://blog.csdn.net/htuhxf/article/details/79954828
```py
>>> i=100
>>> a = 1 if i<100 else 2 if i>100 else 0
>>> a
0
>>> i=101
>>> a = 1 if i<100 else 2 if i>100 else 0
>>> a
2
>>> i=99
>>> a = 1 if i<100 else 2 if i>100 else 0
>>> a
1
```

Python如何一行写完if elif else列表推导式 https://www.jianshu.com/p/654c49562619
- > Python中的if elif else结构通常如下：
  ```py
  if cond1:
      a=1
  elif cond2:
      a=2
  else:
      a=3
  ```
- > 在特殊情况下，我们可能希望把这个条件语句写成一行，如（列表推导式中）。结论就是，将上述结构改为：
  ```console
  非列表：    结果甲 if 条件甲 else 结果乙 if 条件乙 else 结果丙
  列表推导式：    [结果甲 if 条件甲 else 结果乙 if 条件乙 else 结果丙 for xx in list]
  列表推导式筛选包含某个值的数据：    [结果甲 for xx in list if 条件甲]
  ```
