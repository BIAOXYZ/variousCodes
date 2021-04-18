
`27. 移除元素` https://leetcode-cn.com/problems/remove-element/solution/yi-chu-yuan-su-by-leetcode/
- 方法一：双指针
- 方法二：双指针 —— 当要删除的元素很少时

# 测试用例

```
[3,2,2,3]
3
[0,1,2,2,3,0,4,2]
2
```

# C++ vector 遍历中删除（更一般的，迭代器失效问题）
>> //notes：可参见 `000027_algo2.cpp`。总结一下就是，核心点就是`erase()`方法其实是有个返回值的，这个返回值就是其删除的iterator的下一个iterator。所以遍历中删除的话，做到 `000027_algo2.cpp` 注释里说的三点就行：
```cpp
        //   1. for 循环第三项不要搞 ++it，而是在循环体里搞。
        //   2. 需要用 erase 的返回结果给 it 赋值，代表被删除的迭代器 it 的后一个迭代器的值。
        //   3. 不是倒序遍历删除了，而是正序遍历删除。
```
>>> 所以就有个奇怪的问题：**为什么 `000026_Remove_Duplicates_from_Sorted_Array_algo1.cpp` 采用类python的倒序删除法能通过？**这个留着`TODO`吧。。。

c++中vector的遍历及元素删除 https://blog.csdn.net/dds_dev_group/article/details/6951441
```cpp
#include <vector>
#include <iostream>
using namespace std;
int main()
{
    vector<int> test_vec;
    for (int i = 0; i < 5; i++)
    {
        test_vec.push_back(i);
    }
    for(vector<int>::iterator it = test_vec.begin(); it != test_vec.end(); )
    {
        cout<<*(it)<<endl;
        it = test_vec.erase(it);
    }
    cout << "after delete, the length is: " << test_vec.size() << endl;
    return 0;
}
//////////////////////////////////////////////////
0
1
2
3
4
after delete, the length is: 0
```
```cpp
#include <vector>
#include <iostream>
using namespace std;
int main()
{
    vector<int> test_vec;
    for (int i = 0; i < 5; i++)
    {
        test_vec.push_back(i);
    }
    for(vector<int>::iterator it  = test_vec.begin(); it != test_vec.end(); ++it)
    {
        cout<<*(it)<<endl;
        test_vec.erase(it);
    }
    cout << "after delete, the length is: " << test_vec.size() << endl;
    return 0;
//////////////////////////////////////////////////
0
2
4
4
exited, segmentation fault
```
