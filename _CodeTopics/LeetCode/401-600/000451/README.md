
`451. 根据字符出现频率排序` https://leetcode-cn.com/problems/sort-characters-by-frequency/solution/gen-ju-zi-fu-chu-xian-pin-lu-pai-xu-by-l-zmvy/
- [x] 方法一：按照出现频率排序
- [ ] 方法二：桶排序

# 测试用例

```
"tree"
"cccaaa"
"Aabb"
```

# `000451.cpp`

C++ 中的 Lambda 表达式 https://docs.microsoft.com/zh-cn/cpp/cpp/lambda-expressions-in-cpp
- > ISO C++ 标准展示了作为第三个参数传递给 std::sort() 函数的简单 lambda：
  ```cpp
  #include <algorithm>
  #include <cmath>
  void abssort(float* x, unsigned n) {
      std::sort(x, x + n,
          // Lambda expression begins
          [](float a, float b) {
              return (std::abs(a) < std::abs(b));
          } // end of lambda expression
      );
  }
  ```
