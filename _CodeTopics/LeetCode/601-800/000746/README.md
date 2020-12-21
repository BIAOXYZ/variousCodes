
`746. 使用最小花费爬楼梯` https://leetcode-cn.com/problems/min-cost-climbing-stairs/solution/shi-yong-zui-xiao-hua-fei-pa-lou-ti-by-leetcode/

一步一步推导动态规划的多种解法 https://leetcode-cn.com/problems/min-cost-climbing-stairs/solution/yi-bu-yi-bu-tui-dao-dong-tai-gui-hua-de-duo-chong-/

# 测试用例

```
[0,0,0,0]
[10, 15, 20]
[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
```

# `000746_algo2.cpp`

## C++语法点

vector 声明时长度预设 https://blog.csdn.net/leigelaile1/article/details/78580140
```cpp
//vector常见的五种构造函数

    // 0. Create an empty vector v0  
    std::vector<int> v0;  

    // 1. Create a vector v1 with 3 elements of default value 0  
    std::vector<int> v1(3);  

    // 2. Create a vector v2 with 5 elements of value 2  
    std::vector<int> v2(5, 2);  

    // 3. Create a vector v3 with 3 elements of value 1 and with the allocator of vector v2  
    std::vector<int> v3(3, 1, v2.get_allocator());  

    // 4. Create a copy, vector v4, of vector v2  
    std::vector<int> v4(v2);  

    // 5. Create a vector v5 by copying the range v4[_First, _Last)  
    std::vector<int> v5(v4.begin() + 1, v4.begin() + 3);
```
