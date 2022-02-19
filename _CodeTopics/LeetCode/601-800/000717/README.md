
`717. 1比特与2比特字符` https://leetcode-cn.com/problems/1-bit-and-2-bit-characters/solution/1bi-te-yu-2bi-te-zi-fu-by-leetcode-solut-rhrh/
- [x] 方法一：正序遍历
```py
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        i = n - 2
        while i >= 0 and bits[i]:
            i -= 1
        return (n - i) % 2 == 0
```
- [ ] 方法二：倒序遍历

```
[1,0,0]
[1, 1, 1, 0]
```

# 其他

## 1.一个人在官方答案下面评论区贴的代码
//notes：感觉尤其是第一种 `for` 循环那个可以借鉴一下：
- 一是直接在定义 `i` 时也顺便定义了 `n`；
- 二是根据需要跳过某些 `i`。

https://leetcode-cn.com/problems/1-bit-and-2-bit-characters/solution/1bi-te-yu-2bi-te-zi-fu-by-leetcode-solut-rhrh/1389751
- > 【C++】遇到1跳过下一个字符，遇到0跳过本字符。看看是否落到最后
  ```cpp
  class Solution {
  public:
      bool isOneBitCharacter(vector<int>& bits) {
          for(int i = 0, n = bits.size(); i < n; i += bits[i] + 1)
              if(i == n - 1) return true;
          return false;
      }
  };
  ```
- > 想了想倒序是否可行，感觉写起来也挺容易（第一次还没注意题目限定 输入串一定是0结尾）
  ```cpp
  class Solution {
  public:
      bool isOneBitCharacter(vector<int>& bits) {
          return find(rbegin(bits)+1, rend(bits), 0) - rbegin(bits) & 1;
      }
  };
  ```
