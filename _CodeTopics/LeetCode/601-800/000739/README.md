
# 知识点：

- python字典的get()方法
```py
# Python 字典的 get() 方法和 [key] 方法对比 https://blog.csdn.net/aaazz47/article/details/79022644

d = {'a':1,'b':2}
print d.get('c','default value')
print d['c']
--------------------------------------------------
default value
Traceback (most recent call last):
  File "main.py", line 4, in <module>
    print d['c']
KeyError: 'c'
```

https://leetcode-cn.com/problems/daily-temperatures/solution/mei-ri-wen-du-by-leetcode-solution/
- > 方法一：暴力
  * > 反向遍历温度列表。
- > 方法二：单调栈
