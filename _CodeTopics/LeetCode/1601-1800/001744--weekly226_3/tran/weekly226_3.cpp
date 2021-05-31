class Solution {
public:
    vector<bool> canEat(vector<int>& candiesCount, vector<vector<int>>& queries) {
        
        // 此题为第 226 周周赛第三题：
        // https://leetcode-cn.com/contest/weekly-contest-226/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/
        // 原提交为：
        // https://leetcode-cn.com/contest/weekly-contest-226/submissions/detail/142496014/
        // 这里准备翻译成C++版本。

        int length = candiesCount.size();
        vector<unsigned long long int> prefixSum(1, candiesCount[0]);
        for (int i = 1; i < length; ++i) {
            prefixSum.push_back(prefixSum.back() + candiesCount[i]);
        }

        vector<bool> res;
        for (auto query : queries) {
            int typeIndex = query[0], day = query[1], limit = query[2];
            /*
            下面这句最开始是：
                int maxEat = (day + 1) * limit;
            结果不行，报错 “runtime error: signed integer overflow:”。
            
            然后改成下面这句也不行，一样的报错。
                unsigned long long int maxEat = (day + 1) * limit;
            最终证明必须在右边也强转下才行。
            */
            unsigned long long int maxEat = (unsigned long long int)(day + 1) * limit;
            int minEat = day * 1;
            if (typeIndex == 0) {
                if (minEat >= prefixSum[typeIndex]) {
                    res.push_back(false);
                } else {
                    res.push_back(true);
                }
            } else {
                if (maxEat <= prefixSum[typeIndex-1] or minEat >= prefixSum[typeIndex]) {
                    res.push_back(false);
                } else {
                    res.push_back(true);
                }
            }
        }
        return res;
    }
};

/*
https://leetcode-cn.com/submissions/detail/182721506/

62 / 62 个通过测试用例
状态：通过
执行用时: 452 ms
内存消耗: 130.9 MB

执行用时：452 ms, 在所有 C++ 提交中击败了36.51%的用户
内存消耗：130.9 MB, 在所有 C++ 提交中击败了6.35%的用户
*/
