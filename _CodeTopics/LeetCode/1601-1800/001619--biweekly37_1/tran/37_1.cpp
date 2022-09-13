class Solution {
public:
    double trimMean(vector<int>& arr) {
        
        // 第 37 场双周赛第一题
        // https://leetcode-cn.com/submissions/detail/116498842/

        int length = arr.size();
        std::sort(arr.begin(), arr.end());
        int partialLen = length / 20;
        int summ = std::accumulate(arr.begin() + partialLen, arr.end() - partialLen, 0);
        return (double)summ / (length*0.9);
    }
};

/*
https://leetcode.cn/submissions/detail/362646466/

执行用时：
8 ms
, 在所有 C++ 提交中击败了
58.47%
的用户
内存消耗：
9.2 MB
, 在所有 C++ 提交中击败了
17.28%
的用户
通过测试用例：
50 / 50
*/
