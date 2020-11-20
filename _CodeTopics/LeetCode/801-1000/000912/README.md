
`912. 排序数组` https://leetcode-cn.com/problems/sort-an-array/solution/pai-xu-shu-zu-by-leetcode-solution/
- 方法一：快速排序
- 方法二：堆排序
- 方法三：归并排序

Python 实现的十大经典排序算法 https://leetcode-cn.com/problems/sort-an-array/solution/python-shi-xian-de-shi-da-jing-dian-pai-xu-suan-fa/

当我谈排序时，我在谈些什么🤔 https://leetcode-cn.com/problems/sort-an-array/solution/dang-wo-tan-pai-xu-shi-wo-zai-tan-xie-shi-yao-by-s/

# 测试用例

```
[5,2,3,1]
[5,1,1,2,0,0]
```

# 排序算法知识总结

>> //notes：冒泡排序每次把最大的元素排到其位置（最后）；选择排序每次把最小的元素排到其位置（最前）；快速排序每次把某个选定的元素排到其位置。

排序算法 https://zh.wikipedia.org/wiki/%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95 || Sorting algorithm https://en.wikipedia.org/wiki/Sorting_algorithm
- **稳定的排序**：
  * [冒泡排序](https://zh.wikipedia.org/wiki/%E5%86%92%E6%B3%A1%E6%8E%92%E5%BA%8F) (bubble sort)
  * [插入排序](https://zh.wikipedia.org/wiki/%E6%8F%92%E5%85%A5%E6%8E%92%E5%BA%8F) (insertion sort)
  * [桶排序](https://zh.wikipedia.org/wiki/%E6%A1%B6%E6%8E%92%E5%BA%8F) (bucket sort)
  * 计数排序 (counting sort)
  * [归并排序](https://zh.wikipedia.org/wiki/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F) (merge sort)
  * 基数排序 (radix sort)
- **不稳定的排序**：
  * [选择排序](https://zh.wikipedia.org/wiki/%E9%80%89%E6%8B%A9%E6%8E%92%E5%BA%8F) (selection sort)
  * 希尔排序 (shell sort)
  * 堆排序 (heap sort)
  * [快速排序](https://zh.wikipedia.org/wiki/%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F) (quick sort)

## 插入排序

插入排序 https://zh.wikipedia.org/wiki/%E6%8F%92%E5%85%A5%E6%8E%92%E5%BA%8F
- > 插入排序（英语：Insertion Sort）是一种简单直观的排序算法。它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。插入排序在实现上，通常采用in-place排序（即只需用到`O(1)`的额外空间的排序），因而在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。
- > 最早拥有排序概念的机器出现在1901至1904年间由[赫尔曼·何乐礼]()发明出使用基数排序法的分类机，此机器系统包括打孔，制表等功能，1908年分类机第一次应用于人口普查，并且在两年内完成了所有的普查数据和归档。 赫尔曼·何乐礼在1896年创立的分类机公司的前身，为[电脑制表记录公司（CTR）]()。他在电脑制表记录公司曾担任顾问工程师，直到1921年退休，而电脑制表记录公司在1924年正式改名为[IBM]()。
- > Insertion Sort 和打扑克牌时，从牌桌上逐一拿起扑克牌，在手上排序的过程相同。
  ```console
  举例：
  
  Input: {5 2 4 6 1 3}。
  首先拿起第一张牌, 手上有 {5}。
  拿起第二张牌 2, 把 2 insert 到手上的牌 {5}, 得到 {2 5}。
  拿起第三张牌 4, 把 4 insert 到手上的牌 {2 5}, 得到 {2 4 5}。
  
  以此类推。
  ```
- > 此范例程序以C语言实现。
  ```c
  void insertion_sort(int arr[], int len){
          int i,j,key;
          for (i=1;i!=len;++i){
                  key = arr[i];
                  j=i-1;
                  while((j>=0) && (arr[j]>key)) {
                          arr[j+1] = arr[j];
                          j--;
                  }
                  arr[j+1] = key;
          }
  }
  ```

## 归并排序

归并排序 https://zh.wikipedia.org/wiki/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F
- > 归并排序（英语：Merge sort，或mergesort），是创建在归并操作上的一种有效的排序算法，效率为 `O(n*logn)`（大O符号）。1945年由约翰·冯·诺伊曼首次提出。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用，且各层分治递归可以同时进行。
- > **C语言**
  * > 迭代版：
    ```c
    int min(int x, int y) {
        return x < y ? x : y;
    }
    void merge_sort(int arr[], int len) {
        int *a = arr;
        int *b = (int *) malloc(len * sizeof(int));
        int seg, start;
        for (seg = 1; seg < len; seg += seg) {
            for (start = 0; start < len; start += seg * 2) {
                int low = start, mid = min(start + seg, len), high = min(start + seg * 2, len);
                int k = low;
                int start1 = low, end1 = mid;
                int start2 = mid, end2 = high;
                while (start1 < end1 && start2 < end2)
                    b[k++] = a[start1] < a[start2] ? a[start1++] : a[start2++];
                while (start1 < end1)
                    b[k++] = a[start1++];
                while (start2 < end2)
                    b[k++] = a[start2++];
            }
            int *temp = a;
            a = b;
            b = temp;
        }
        if (a != arr) {
            int i;
            for (i = 0; i < len; i++)
                b[i] = a[i];
            b = a;
        }
        free(b);
    }
    ```
  * > 递归版：
    ```c
    void merge_sort_recursive(int arr[], int reg[], int start, int end) {
        if (start >= end)
            return;
        int len = end - start, mid = (len >> 1) + start;
        int start1 = start, end1 = mid;
        int start2 = mid + 1, end2 = end;
        merge_sort_recursive(arr, reg, start1, end1);
        merge_sort_recursive(arr, reg, start2, end2);
        int k = start;
        while (start1 <= end1 && start2 <= end2)
            reg[k++] = arr[start1] < arr[start2] ? arr[start1++] : arr[start2++];
        while (start1 <= end1)
            reg[k++] = arr[start1++];
        while (start2 <= end2)
            reg[k++] = arr[start2++];
        for (k = start; k <= end; k++)
            arr[k] = reg[k];
    }

    void merge_sort(int arr[], const int len) {
        int reg[len];
        merge_sort_recursive(arr, reg, 0, len - 1);
    }
    ```
- > **Python3**
  ```py
  def mergeSort(nums):
      if len(nums) < 2:
          return nums
      mid = len(nums) // 2
      left = mergeSort(nums[:mid])
      right = mergeSort(nums[mid:])
      result = []
      while left and right:
          if left[0] <= right[0]:
              result.append(left.pop(0))
          else:
              result.append(right.pop(0))
      if left:
          result += left
      if right:
          result += right
      return result
  
  if __name__ == "__main__":
      nums = [1, 4, 2, 3.6, -1, 0, 25, -34, 8, 9, 1, 0]
      print("original:", nums)
      print("Sorted:", mergeSort(nums))
  ```

## 选择排序

选择排序 https://zh.wikipedia.org/wiki/%E9%80%89%E6%8B%A9%E6%8E%92%E5%BA%8F
- > 选择排序（Selection sort）是一种简单直观的排序算法。它的工作原理如下。首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。
- > 选择排序的主要优点与数据移动有关。如果某个元素位于正确的最终位置上，则它不会被移动。选择排序每次交换一对元素，它们当中至少有一个将被移到其最终位置上，因此对 n 个元素的表进行排序总共进行至多 n-1 次交换。在所有的完全依靠交换去移动元素的排序方法中，选择排序属于非常好的一种。
- > 实现示例（Python）
  ```py
  def selection_sort(arr):
      for i in range(len(arr)-1):
          minIndex=i
          for j in range(i+1,len(arr)):
              if arr[minIndex]>arr[j]:
                  minIndex=j
          if i==minIndex:
              pass
          else:
              arr[i],arr[minIndex]=arr[minIndex],arr[i]
      return arr

  if __name__ == '__main__':
      testlist = [17, 23, 20, 14, 12, 25, 1, 20, 81, 14, 11, 12]
      print(selection_sort(testlist))
  ```

## 快速排序

快速排序 https://zh.wikipedia.org/wiki/%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F
- > 快速排序（英语：Quicksort），又称分区交换排序（partition-exchange sort），简称快排，一种排序算法，最早由东尼·霍尔提出。
- > 分割：重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面（与基准值相等的数可以到任何一边）。在这个分割结束之后，***对基准值的排序就已经完成***。
- > 递归到最底部的判断条件是数列的大小是零或一，此时该数列显然已经有序。
- > 快速排序是二叉查找树（二叉搜索树）的一个空间最优化版本。不是循序地把数据项插入到一个明确的树中，而是由快速排序组织这些数据项到一个由递归调用所隐含的树中。这两个算法完全地产生相同的比较次数，但是顺序不同。对于排序算法的稳定性指标，原地分割版本的快速排序算法是不稳定的。其他变种是可以通过牺牲性能和空间来维护稳定性的。
- > 快速排序的最直接竞争者是堆排序（Heapsort）。堆排序通常比快速排序稍微慢，但是最坏情况的运行时间总是`O(n\log n)`。快速排序是经常比较快，除了introsort变化版本外，仍然有最坏情况性能的机会。如果事先知道堆排序将会是需要使用的，那么直接地使用堆排序比等待introsort再切换到它还要快。堆排序也拥有重要的特点，仅使用固定额外的空间（堆排序是原地排序），而即使是最佳的快速排序变化版本也需要`\Theta (\log n)`的空间。然而，堆排序需要有效率的随机存取才能变成可行。
- > 快速排序也与归并排序（Mergesort）竞争，这是另外一种递归排序算法，但有坏情况`O(n\log n)`运行时间的优势。不像快速排序或堆排序，归并排序是一个稳定排序，且可以轻易地被采用在链表（linked list）和存储在慢速访问媒体上像是磁盘存储或网络连接存储的非常巨大数列。尽管快速排序可以被重新改写使用在链串列上，但是它通常会因为无法随机存取而导致差的基准选择。归并排序的主要缺点，是在最佳情况下需要`\Omega (n)`额外的空间。

算法 3：最常用的排序——快速排序 https://wiki.jikexueyuan.com/project/easy-learn-algorithm/fast-sort.html
- > ![](https://wiki.jikexueyuan.com/project/easy-learn-algorithm/images/3.1.png)
