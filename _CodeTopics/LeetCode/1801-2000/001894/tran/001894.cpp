class Solution {
public:
    int chalkReplacer(vector<int>& chalk, int k) {
        
        // 这道题Python做意义没有C系列的大，因为Python不用管溢出。。。
        // 用 int 应该肯定不行，这里先用 long 试一把——大概率也是会溢出的。

        // 注意：除了 remainder 定义时类型选成 long long，求和里的 0 也要写成 0LL 或 0ll，不然照样溢出。
        long long remainder = k % std::accumulate(chalk.begin(), chalk.end(), 0ll);
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
https://leetcode-cn.com/submissions/detail/217365241/

72 / 72 个通过测试用例
状态：通过
执行用时: 112 ms
内存消耗: 72.6 MB

执行用时：112 ms, 在所有 C++ 提交中击败了93.33%的用户
内存消耗：72.6 MB, 在所有 C++ 提交中击败了65.11%的用户
*/
