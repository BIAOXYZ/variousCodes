class Solution {
public:
    vector<int> goodDaysToRobBank(vector<int>& security, int time) {

        // 第 67 场双周赛第二题
        // https://leetcode-cn.com/submissions/detail/247596451/ --> 对着这个翻译完，自己都晕了。

        int n = security.size();
        if (n < 2 * time + 1)
            return vector<int>{};
        
        vector<int> leftinds = {};
        int leftind1 = 0;
        bool inWindowState = false;
        while (leftind1 < n - 2*time) {
            int leftind2 = leftind1 + time;
            if (!inWindowState) {
                bool breakflag = false;
                for (int i = leftind1; i < leftind2; ++i) {
                    if (security[i] >= security[i+1]) {
                        continue;
                    } else {
                        breakflag = true;
                        leftind1 = i + 1;
                        break;
                    }
                }
                if (!breakflag) {
                    inWindowState = true;
                    leftinds.push_back(leftind1);
                    ++leftind1;
                }
            } else {
                if (security[leftind2 - 1] >= security[leftind2]) {
                    leftinds.push_back(leftind1);
                    ++leftind1;
                } else {
                    inWindowState = false;
                    leftind1 = leftind2;
                }
            }
        }

        vector<int> rightinds = {};
        int rightind1 = time;
        inWindowState = false;
        while (rightind1 < n - time) {
            int rightind2 = rightind1 + time;
            if (!inWindowState) {
                bool breakflag = false;
                for (int i = rightind1; i < rightind2; ++i) {
                    if (security[i] <= security[i+1]) {
                        continue;
                    } else {
                        breakflag = true;
                        rightind1 = i + 1;
                        break;
                    }
                }
                if (!breakflag) {
                    inWindowState = true;
                    rightinds.push_back(rightind1 + 1);
                    ++rightind1;
                }
            } else {
                if (security[rightind2 - 1] <= security[rightind2]) {
                    rightinds.push_back(rightind1 + 1);
                    ++rightind1;
                } else {
                    inWindowState = false;
                    rightind1 = rightind2;
                }
            }
        }

        unordered_set<int> tmp_rightinds = unordered_set<int>(rightinds.begin(), rightinds.end());
        vector<int> res;
        for (int ind : leftinds) {
            if (tmp_rightinds.find(ind + time + 1) != tmp_rightinds.end()) {
                res.push_back(ind + time);
            }
        }
        return res;
    }
};

/*
https://leetcode-cn.com/submissions/detail/277985399/

执行用时：144 ms, 在所有 C++ 提交中击败了12.60%的用户
内存消耗：98.3 MB, 在所有 C++ 提交中击败了5.08%的用户
通过测试用例：
144 / 144
*/
