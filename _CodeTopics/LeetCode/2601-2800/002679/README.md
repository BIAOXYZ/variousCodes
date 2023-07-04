
`2679. 矩阵中的和` https://leetcode.cn/problems/sum-in-a-matrix/solution/ju-zhen-zhong-de-he-by-leetcode-solution-88bx/
- [ ] 方法一：模拟
- [x] 方法二：排序 

https://leetcode.cn/problems/sum-in-a-matrix/solution/ju-zhen-zhong-de-he-by-leetcode-solution-88bx/2056139
- > 善用map
  ```py
  class Solution:
      def matrixSum(self, nums: List[List[int]]) -> int:
          return sum(map(max, zip(*map(sorted, nums))))
  ```

```
[[7,2,1],[6,4,2],[6,5,3],[3,2,1]]
[[1]]
```
