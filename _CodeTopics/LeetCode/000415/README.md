
`字符串相加` https://leetcode-cn.com/problems/add-strings/solution/zi-fu-chuan-xiang-jia-by-leetcode-solution/

字符串相加 （双指针，清晰图解） https://leetcode-cn.com/problems/add-strings/solution/add-strings-shuang-zhi-zhen-fa-by-jyd/
>> //notes: 这哥们python的代码比我的简单不少。
  ```py3
  class Solution:
      def addStrings(self, num1: str, num2: str) -> str:
          res = ""
          i, j, carry = len(num1) - 1, len(num2) - 1, 0
          while i >= 0 or j >= 0:
              n1 = int(num1[i]) if i >= 0 else 0
              n2 = int(num2[j]) if j >= 0 else 0
              tmp = n1 + n2 + carry
              carry = tmp // 10
              res = str(tmp % 10) + res
              i, j = i - 1, j - 1
          return "1" + res if carry else res
  ```
但是后来发现，ta可能是仿着官方c++答案来的：
  ```cpp
  class Solution {
  public:
      string addStrings(string num1, string num2) {
          int i = num1.length() - 1, j = num2.length() - 1, add = 0;
          string ans = "";
          while (i >= 0 || j >= 0 || add != 0) {
              int x = i >= 0 ? num1[i] - '0' : 0;
              int y = j >= 0 ? num2[j] - '0' : 0;
              int result = x + y + add;
              ans.push_back('0' + result % 10);
              add = result / 10;
              i -= 1;
              j -= 1;
          }
          // 计算完以后的答案需要翻转过来
          reverse(ans.begin(), ans.end());
          return ans;
      }
  };
  ```
