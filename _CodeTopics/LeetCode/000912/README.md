
`912. 排序数组` https://leetcode-cn.com/problems/sort-an-array/solution/pai-xu-shu-zu-by-leetcode-solution/
- 方法一：快速排序
- 方法二：堆排序
- 方法三：归并排序

Python 实现的十大经典排序算法 https://leetcode-cn.com/problems/sort-an-array/solution/python-shi-xian-de-shi-da-jing-dian-pai-xu-suan-fa/

当我谈排序时，我在谈些什么🤔 https://leetcode-cn.com/problems/sort-an-array/solution/dang-wo-tan-pai-xu-shi-wo-zai-tan-xie-shi-yao-by-s/

# 排序算法知识总结

>> //notes：冒泡排序每次把最大的元素排到其位置（最后）；选择排序每次把最小的元素排到其位置（最前）；快速排序每次把某个选定的元素排到其位置。

排序算法 https://zh.wikipedia.org/wiki/%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95 || Sorting algorithm https://en.wikipedia.org/wiki/Sorting_algorithm
- **稳定的排序**：
  * 冒泡排序 https://zh.wikipedia.org/wiki/%E5%86%92%E6%B3%A1%E6%8E%92%E5%BA%8F
- **不稳定的排序**：
  * [选择排序](https://zh.wikipedia.org/wiki/%E9%80%89%E6%8B%A9%E6%8E%92%E5%BA%8F)
  * [快速排序](https://zh.wikipedia.org/wiki/%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F)

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

快速排序 https://zh.wikipedia.org/wiki/%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F
- > 快速排序（英语：Quicksort），又称分区交换排序（partition-exchange sort），简称快排，一种排序算法，最早由东尼·霍尔提出。
- > 分割：重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面（与基准值相等的数可以到任何一边）。在这个分割结束之后，***对基准值的排序就已经完成***。
- > 递归到最底部的判断条件是数列的大小是零或一，此时该数列显然已经有序。
- > 快速排序是二叉查找树（二叉搜索树）的一个空间最优化版本。不是循序地把数据项插入到一个明确的树中，而是由快速排序组织这些数据项到一个由递归调用所隐含的树中。这两个算法完全地产生相同的比较次数，但是顺序不同。对于排序算法的稳定性指标，原地分割版本的快速排序算法是不稳定的。其他变种是可以通过牺牲性能和空间来维护稳定性的。
- > 快速排序的最直接竞争者是堆排序（Heapsort）。堆排序通常比快速排序稍微慢，但是最坏情况的运行时间总是`O(n\log n)`。快速排序是经常比较快，除了introsort变化版本外，仍然有最坏情况性能的机会。如果事先知道堆排序将会是需要使用的，那么直接地使用堆排序比等待introsort再切换到它还要快。堆排序也拥有重要的特点，仅使用固定额外的空间（堆排序是原地排序），而即使是最佳的快速排序变化版本也需要`\Theta (\log n)`的空间。然而，堆排序需要有效率的随机存取才能变成可行。
- > 快速排序也与归并排序（Mergesort）竞争，这是另外一种递归排序算法，但有坏情况`O(n\log n)`运行时间的优势。不像快速排序或堆排序，归并排序是一个稳定排序，且可以轻易地被采用在链表（linked list）和存储在慢速访问媒体上像是磁盘存储或网络连接存储的非常巨大数列。尽管快速排序可以被重新改写使用在链串列上，但是它通常会因为无法随机存取而导致差的基准选择。归并排序的主要缺点，是在最佳情况下需要`\Omega (n)`额外的空间。
