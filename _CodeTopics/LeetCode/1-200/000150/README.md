
`150. 逆波兰表达式求值` https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/solution/ni-bo-lan-biao-da-shi-qiu-zhi-by-leetcod-wue9/
- [x] 方法一：栈
- [ ] 方法二：数组模拟栈

# 测试用例 

```
["2","1","+","3","*"]
["4","13","5","/","+"]
["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
["6","2","/"]
["6","4","/"]
["5","3","/"]
["6","-2","/"]
["6","-4","/"]
["5","-3","/"]
```

# `000150.py`

```py
print 6/-132
print 6/132
print "**********"
print 6/(-132*1.0)
print int(6/(-132*1.0))
print "**********"
print 6/3, 6/-3
print 6/4, 6/-4
print 5/3, 5/-3
--------------------------------------------------
-1
0
**********
-0.0454545454545
0
**********
2 -2
1 -2
1 -2
```

以最后一个，也就是`5/-3`为例。正常python计算结果是-2，但是答案里都是向上取整，所以答案里这个除结果是-1。也就是一旦发生***一正一负做除法且除不尽时***，按原版结果加1就行。

# `000150_impl.cpp`

## 里面很多C++的语法知识点，主要包括：
- STL `stack`：
  * `stack`判断为空应该是 `.empty()` 方法，而不是和空指针比较（Python影响的）。。。
  * `.pop()` 方法返回值为空，要想拿栈顶元素应该 `.top()` 方法
- STL `string`：
  * `.c_str()`，转换完成后才能用例如 `atoi()` 之类的函数。
  * `.length()` 和 `.size()` 除了名字不一样，其他完全一模一样。
    + https://www.geeksforgeeks.org/5-different-methods-find-length-string-c/
- C++ 本身：
  * 过长的行换行也是末尾加反斜杠 `\`，新行同样可以不用考虑缩进之类的（Python换行都不用考虑了，何况C++）
    + https://stackoverflow.com/questions/969394/how-to-split-long-lines-of-code-in-c 
  * `atoi()` 和 `isdigit()`
  * 注意单引号是字符，双引号是字符串，所以这句 `else if (tk[0] == '-') stk.push(leftNum - rightNum);` 里面用双引号是不行的，又是Python的影响。
