
二进制求和 https://leetcode-cn.com/problems/add-binary/solution/er-jin-zhi-qiu-he-by-leetcode-solution/
- > 方法二：位运算
  ```
  如果不了解位运算，可以先了解位运算并尝试练习以下题目：

  只出现一次的数字 II
  只出现一次的数字 III
  数组中两个数的最大异或值
  重复的DNA序列
  最大单词长度乘积
  ```
- > 为什么这个方法是可行的呢？在第一轮计算中，`answer` 的最后一位是 x 和 y 相加之后的结果，`carry` 的倒数第二位是 x 和 y 最后一位相加的进位。接着每一轮中，由于 `carry` 是由 x 和 y 按位与并且左移得到的，那么最后会补零，所以在下面计算的过程中后面的数位不受影响，而每一轮都可以得到一个低 i 位的答案和它向低 i + 1 位的进位，也就模拟了加法的过程。
  ```py3
  class Solution:
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]
  ```

关于加法器：
- 加法器 https://zh.wikipedia.org/wiki/%E5%8A%A0%E6%B3%95%E5%99%A8
- 四位计算机的原理及其实现 http://www.ruanyifeng.com/blog/2011/03/4-bit_computer.html
- 加法器原理浅析及编程模拟 https://liamlin.me/2019/06/27/the-principle-and-programming-simulation-of-binary-adder
