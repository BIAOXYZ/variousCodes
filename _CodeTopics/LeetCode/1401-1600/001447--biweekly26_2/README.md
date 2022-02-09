
`1447. 最简分数` https://leetcode-cn.com/problems/simplified-fractions/solution/zui-jian-fen-shu-by-leetcode-solution-98zy/
- [x] 方法一：数学

```
1
2
3
4
```

# 官方答案

C++原生的最大公约数函数是 `__gcd()`。
```cpp
class Solution {
public:
    vector<string> simplifiedFractions(int n) {
        vector<string> ans;
        for (int denominator = 2; denominator <= n; ++denominator) {
            for (int numerator = 1; numerator < denominator; ++numerator) {
                if (__gcd(numerator, denominator) == 1) {
                    ans.emplace_back(to_string(numerator) + "/" + to_string(denominator));
                }
            }
        }
        return ans;
    }
};
```
