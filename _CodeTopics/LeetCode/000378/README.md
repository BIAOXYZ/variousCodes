
378. 有序矩阵中第K小的元素 https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/solution/you-xu-ju-zhen-zhong-di-kxiao-de-yuan-su-by-leetco/
- 方法一：直接排序
- [x] 方法二：归并排序
- 方法三：二分查找
  * > 
    ```py
    class Solution:
        def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
            n = len(matrix)

            def check(mid):
                i, j = n - 1, 0
                num = 0
                while i >= 0 and j < n:
                    if matrix[i][j] <= mid:
                        num += i + 1
                        j += 1
                    else:
                        i -= 1
                return num >= k

            left, right = matrix[0][0], matrix[-1][-1]
            while left < right:
                mid = (left + right) // 2
                if check(mid):
                    right = mid
                else:
                    left = mid + 1

            return left
    ```

使用堆(heap)(官解中的"归并排序")思路详解；另附Python heapq模块用法解释 https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/solution/shi-yong-dui-heapde-si-lu-xiang-jie-ling-fu-python/

值域的二分查找 https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/solution/dui-shu-zhi-er-fen-cha-zhao-by-hyj8/
