
`409. 最长回文串` https://leetcode-cn.com/problems/longest-palindrome/solution/zui-chang-hui-wen-chuan-by-leetcode-solution/
- [x] 方法一：贪心 【其实主要是哈希表吧，或者至少 贪心+哈希表】

# 测试用例

```
"abccccdd"
"x"
"xxyyy"
```

# 语法点（主要是`000409_iii.cpp`的代码，去了些空行之类的。）

TODO：为什么下面代码里用引用的时候（`&pr`）必须得有`const`关键字修饰？

```cpp
class Solution {
public:
    int longestPalindrome(string s) {
        unordered_map<char, int> dic;
        for (char ch : s) {
            if (dic.find(ch) != dic.end()) {
                dic[ch]++;
            } else {
                dic[ch] = 1;
            }
        }

        int res = 0;
        bool flag = false;
        /*
        - 这里当然也可以用 for (auto &pr : dic)，但是我发现如果用 for (std::pair<char, int> &pr : dic)，
          也就是少了 const，也是不行的。。。
        - 但是我如果去掉引用符号 &，那么就可以不带 const 了（当然带上 const 也没问题）。
        */
        for (std::pair<char, int> &pr : dic) {
            if (pr.second % 2 == 0) {
                res += pr.second;
            } else {
                flag = true;
                res += pr.second - 1;
            }
        }

        if (!flag) {
            return res;
        } else {
            return res + 1;
        }
    }
};
```

```console
Line 21: Char 36: error: non-const lvalue reference to type 'pair<char, [...]>' cannot bind to a value of unrelated type 'pair<const char, [...]>'
        for (std::pair<char, int> &pr : dic) {
                                   ^  ~
/usr/bin/../lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/bits/unordered_map.h:324:7: note: selected 'begin' function with iterator type 'std::unordered_map<char, int, std::hash<char>, std::equal_to<char>, std::allocator<std::pair<const char, int>>>::iterator' (aka '_Node_iterator<std::pair<const char, int>, __constant_iterators::value, __hash_cached::value>')
      begin() noexcept
      ^
1 error generated.
```
