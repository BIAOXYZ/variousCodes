class Solution {
public:
    int totalMoney(int n) {
        
        // 第 43 场双周赛第一题
        // https://leetcode-cn.com/submissions/detail/137229132/

        int quotient = n / 7, remainder = n % 7;
        vector<int> v{1,2,3,4,5,6,7};
        int partSum = std::accumulate(v.begin(), v.end(), 0);
        int startNum = 1;

        int res = 0;
        for (int i = 0; i < quotient; ++i) {
            res += partSum;
            partSum += 7;
            startNum += 1;
        }
        for (int j = 0; j < remainder; ++j) {
            res += startNum;
            startNum += 1;
        }
        return res;
    }
};

/*
https://leetcode-cn.com/submissions/detail/258577707/

执行用时：0 ms, 在所有 C++ 提交中击败了100.00%的用户
内存消耗：5.9 MB, 在所有 C++ 提交中击败了5.39%的用户
通过测试用例：
106 / 106
*/
