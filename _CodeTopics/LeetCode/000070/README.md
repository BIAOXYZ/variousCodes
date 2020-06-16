
爬楼梯 https://leetcode-cn.com/problems/climbing-stairs/solution/pa-lou-ti-by-leetcode-solution/
- 方法一：动态规划
- 方法二：矩阵快速幂
- 方法三：通项公式

# 方法二：矩阵快速幂

官方代码（只有Java）如下：
```java
public class Solution {
   public int climbStairs(int n) {
       int[][] q = {{1, 1}, {1, 0}};
       int[][] res = pow(q, n);
       return res[0][0];
   }
   public int[][] pow(int[][] a, int n) {
       int[][] ret = {{1, 0}, {0, 1}};
       while (n > 0) {
           if ((n & 1) == 1) {
               ret = multiply(ret, a);
           }
           n >>= 1;
           a = multiply(a, a);
       }
       return ret;
   }
   public int[][] multiply(int[][] a, int[][] b) {
       int[][] c = new int[2][2];
       for (int i = 0; i < 2; i++) {
           for (int j = 0; j < 2; j++) {
               c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j];
           }
       }
       return c;
   }
}
```
那个`return res[0][0];`很容易引起误解：为什么只把幂数矩阵n次方，然后返回其`[0][0]号元素`就可以了？也就是为什么这个`[0][0]号元素`就是`f(n)`呢？解释如下：
```console
// 下面分别的是幂数矩阵q的1次方到5次方，按理说假如我求f(5)，我应该 q^4 再右乘上 |f(1),f(0)|^T，也就是|1 1|^T。
// 然后取结果列矩阵的第一个元素。
// 但是矩阵1乘矩阵2，结果矩阵3的每一列其实就是矩阵1乘以矩阵2的每一列，而恰好q的第一列就是|1 1|^T。

|1 1|
|1 0|

|2 1|
|1 1|

|3 2|
|2 1|

|5 3|
|3 2|

|8 5|
|5 3|
```
