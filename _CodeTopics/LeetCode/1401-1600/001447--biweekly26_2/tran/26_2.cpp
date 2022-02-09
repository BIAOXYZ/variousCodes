class Solution {
public:
    vector<string> simplifiedFractions(int n) {

        // 第 26 场双周赛第二题
        // https://leetcode-cn.com/submissions/detail/71323563/

        // 比赛时的版本用了两个Python内部的函数，正好这里可以同时
        // 写两种版本的 C++ lambda 匿名函数。
        std::function<int(int, int)> gcd = [](int a, int b) -> int {
            if (a < b) {
                int tmp = a; a = b; b = tmp;
            }
            while (b > 0) {
                int remainder = a % b;
                a = b; b = remainder;
            }
            return a;
        };
        
        // 对于外部的非变量对象（这里是函数gcd）也需要引用，
        //// 不然到 “if (gcd(i, n) == 1) {” 这行会报错。
        // 此外，通用的引用形式当然也是可以的：
        //// “auto exactN = [&](int n) {”
        auto exactN = [&gcd](int n) {
            vector<string> listn = {};
            for (int i = 1; i < n; ++i) {
                if (gcd(i, n) == 1) {
                    string s = to_string(i) + "/" + to_string(n);
                    listn.emplace_back(s);
                }
            }
            return listn;
        };

        vector<string> res;
        for (int i = 2; i < n + 1; ++i) {
            vector<string> tmpVec = exactN(i);
            // vector 合并的方法，类似 Python list 的 extend 或者 list 直接想加。
            res.insert(res.end(), tmpVec.begin(), tmpVec.end());
        }
        return res;
    }
};

/*
https://leetcode-cn.com/submissions/detail/266460472/

执行用时：64 ms, 在所有 C++ 提交中击败了31.48%的用户
内存消耗：33.6 MB, 在所有 C++ 提交中击败了5.55%的用户
通过测试用例：
100 / 100
*/
