class Solution {
public:
    int minStartValue(vector<int>& nums) {

        // 第 24 场双周赛第一题
        // https://leetcode.cn/submissions/detail/64010550/

        int startValue = 1;
        int sum = startValue;
        for (int num : nums) {
            sum += num;
            if (sum <= 0) {
                startValue = startValue + 1 - sum;
                sum = 1; 
            }
        }
        return startValue;
    }
};

/*
https://leetcode.cn/submissions/detail/348123191/

执行用时：
0 ms
, 在所有 C++ 提交中击败了
100.00%
的用户
内存消耗：
7.2 MB
, 在所有 C++ 提交中击败了
23.73%
的用户
通过测试用例：
55 / 55
*/
