
`389. 找不同` https://leetcode-cn.com/problems/find-the-difference/solution/zhao-bu-tong-by-leetcode-solution-mtqf/
- [x] 方法一：计数
- 方法二：求和
- 方法三：位运算

# 测试用例

```
"abcd"
"abcde"
""
"y"
"a"
"aa"
"ae"
"aea"
```

# `000389.cpp`

语法点：
- c++的范围for循环：`for (auto ch : s){}`
- c++的`unordered_map`的查找方法`.find()`和遍历方法`.begin()`。

C++11新特性之基本范围的For循环（range-based-for） https://blog.csdn.net/hailong0715/article/details/54172848
- > 但是需要注意的在上述对容器的遍历是只读的，也就是说遍历的值是不可修改的，看下面例子：
```cpp
std::vector<int> vec {1,2,3,4,5,6,7,8,9,10};
cout << "修改前" << endl;
for (auto n :vec)
    std::cout << n++;

cout << endl;

cout << "修改后" << endl;
for (auto j : vec)
    std::cout << j;
```
- > 在上述例子中，我们首先遍历容器的内容，然后给容器内的元素每个都加1，然后再遍历一次容器的内容，示例的输出结果如下：
```console
修改前
12345678910
修改后
12345678910
```
- > 那么如果要遍历容器内的元素的同时又要修改元素的值该怎么做呢，方法就是将遍历的变量声明为引用类型，看下面例子：
```cpp
std::vector<int> vec {1,2,3,4,5,6,7,8,9,10};
cout << "修改前" << endl;
for (auto& n :vec)
	std::cout << n++;

cout << endl;

cout << "修改后" << endl;
for (auto j : vec)
	std::cout << j;
```
- > 代码的输出结果为：
```console
修改前
12345678910
修改后
234567891011
```

C++ for 循环 https://www.runoob.com/cplusplus/cpp-for-loop.html
- >
  ```cpp
  int my_array[5] = {1, 2, 3, 4, 5};
  // 每个数组元素乘于 2
  for (int &x : my_array)
  {
      x *= 2;
      cout << x << endl;  
  }
  // auto 类型也是 C++11 新标准中的，用来自动获取变量的类型
  for (auto &x : my_array) {
      x *= 2;
      cout << x << endl;  
  }
  ```
- > 上面for述句的第一部分定义被用来做范围迭代的变量，就像被声明在一般for循环的变量一样，其作用域仅只于循环的范围。而在":"之后的第二区块，代表将被迭代的范围。
