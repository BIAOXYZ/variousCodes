
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

## C++匿名函数

Lambda expressions (since C++11) https://en.cppreference.com/w/cpp/language/lambda

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

现代 C++：Lambda 表达式 - FOCUS的文章 - 知乎 https://zhuanlan.zhihu.com/p/150554945

## C++ unordered_map 列出全部key或者value的接口
>> //notes： C++ unordered_map 没有类似 Python 的 .keys(), .values() 接口。。。只能自己实现- -于是自己实现了一个：
```cpp
    vector<char> get_list_of_keys(unordered_map<char, int> ump) {
        vector<char> res;
        for (auto kv : ump) {
            res.push_back(kv.first);
        }
        return res;
    }
```
// 后来又在网上找了一个，见下一个实现的笔记。

# `000451_ii.cpp`

https://stackoverflow.com/questions/8483985/obtaining-list-of-keys-and-values-from-unordered-map/33941694#33941694
- > Joining late, but thought this might be helpful to someone. Two template functions making use of `key_type` and `mapped_type`.
```cpp
namespace mapExt
{
    template<typename myMap>
    std::vector<typename myMap::key_type> Keys(const myMap& m)
    {
        std::vector<typename myMap::key_type> r;
        r.reserve(m.size());
        for (const auto&kvp : m)
        {
            r.push_back(kvp.first);
        }
        return r;
    }

    template<typename myMap>
    std::vector<typename myMap::mapped_type> Values(const myMap& m)
    {
        std::vector<typename myMap::mapped_type> r;
        r.reserve(m.size());
        for (const auto&kvp : m)
        {
            r.push_back(kvp.second);
        }
        return r;
    }
}
```
- > Usage:
```cpp
std::map<long, char> mO;
std::unordered_map<long, char> mU;
// set up the maps
std::vector<long> kO = mapExt::Keys(mO);
std::vector<long> kU = mapExt::Keys(mU);
std::vector<char> vO = mapExt::Values(mO);
std::vector<char> vU = mapExt::Values(mU);
```
