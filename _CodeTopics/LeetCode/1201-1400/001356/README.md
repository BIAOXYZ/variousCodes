
`1356. 根据数字二进制下 1 的数目排序` https://leetcode-cn.com/problems/sort-integers-by-the-number-of-1-bits/solution/gen-ju-shu-zi-er-jin-zhi-xia-1-de-shu-mu-pai-xu-by/
- [x] 方法一：暴力
- 方法二：递推预处理

https://leetcode-cn.com/problems/sort-integers-by-the-number-of-1-bits/comments/252552
- >
  ```py3
  class Solution:
      def sortByBits(self, arr: List[int]) -> List[int]:
          return sorted(arr,key=lambda x:(bin(x).count('1'),x))
  ```
- > 能不能讲讲这个lambda的写法是什么意思？
  >> sorted()函数里这个参数key接收一个匿名函数。先按照二进制中1的个数排序(bin(x).count('1'))，再按照数值大小排序(x)。

# 测试用例

```
[0,1,2,3,4,5,6,7,8]
[1024,512,256,128,64,32,16,8,4,2,1]
[10000,10000]
[2,3,5,7,11,13,17,19]
```
