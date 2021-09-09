class Solution {
public:
    int chalkReplacer(vector<int>& chalk, int k) {
        
        // 这道题Python做意义没有C系列的大，因为Python不用管溢出。。。
        // 用 int 应该肯定不行，这里先用 long 试一把——大概率也是会溢出的。
        long remainder = k % std::accumulate(chalk.begin(), chalk.end(), 0);
        for (int i = 0; i < chalk.size(); ++i) {
            if (remainder < chalk[i])
                return i;
            else
                remainder -= chalk[i];
        }
        // Python实现里就不用这句，但是C++我也没办法控制leetcode的编译参数，所以加了这句。不然会报如下错误：
        // Line 15: Char 5: error: non-void function does not return a value in all control paths [-Werror,-Wreturn-type] }
        return -1;
    }
};

/*
https://leetcode-cn.com/submissions/detail/217364343/

60 / 72 个通过测试用例
状态：执行出错

执行出错信息：
Line 130: Char 39: runtime error: signed integer overflow: 2147423110 + 92123 cannot be represented in type 'int' (stl_numeric.h)
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior /usr/bin/../lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/bits/stl_numeric.h:139:39

最后执行的输入：
*/
