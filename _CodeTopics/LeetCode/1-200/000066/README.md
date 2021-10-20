
`66. 加一` https://leetcode-cn.com/problems/plus-one/solution/jia-yi-by-leetcode-solution-2hor/
- [ ] 方法一：找出最长的后缀 99

# 测试用例

```
[1,2,3]
[4,3,2,1]
[0]
[9]
[9,9]
```

# 语法

## C++ vector 在指定位置插入元素

C++ STL vector插入元素（insert()和emplace()）详解 http://c.biancheng.net/view/6834.html
```cpp
#include <iostream> 
#include <vector> 
#include <array> 
using namespace std;
int main()
{
    std::vector<int> demo{1,2};
    //第一种格式用法
    demo.insert(demo.begin() + 1, 3);//{1,3,2}
    //第二种格式用法
    demo.insert(demo.end(), 2, 5);//{1,3,2,5,5}
    //第三种格式用法
    std::array<int,3>test{ 7,8,9 };
    demo.insert(demo.end(), test.begin(), test.end());//{1,3,2,5,5,7,8,9}
    //第四种格式用法
    demo.insert(demo.end(), { 10,11 });//{1,3,2,5,5,7,8,9,10,11}
    for (int i = 0; i < demo.size(); i++) {
        cout << demo[i] << " ";
    }
    return 0;
}
/////////////////////////////////////////////
运行结果为：
1 3 2 5 5 7 8 9 10 11
```
