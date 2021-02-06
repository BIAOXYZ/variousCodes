class Solution {
public:
    int maxScore(vector<int>& cardPoints, int k) {

        int total = accumulate(cardPoints.begin(), cardPoints.end(), 0);
        int length = cardPoints.size();
        if (k == length)
            return total;
        
        int n = length - k;
        int currSum = accumulate(cardPoints.begin(), cardPoints.begin() + n, 0);
        int minSum = currSum;
        for (int i = 1; i < length - n + 1; ++i) {
            currSum += cardPoints[i+n-1] - cardPoints[i-1];
            minSum = min(minSum, currSum);
        }
        return total - minSum;

    }
};

/*
https://leetcode-cn.com/submissions/detail/144153595/

40 / 40 个通过测试用例
状态：通过
执行用时: 76 ms
内存消耗: 41.3 MB

执行用时：76 ms, 在所有 C++ 提交中击败了79.69%的用户
内存消耗：41.3 MB, 在所有 C++ 提交中击败了97.29%的用户
*/
