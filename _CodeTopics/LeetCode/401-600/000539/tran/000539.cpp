class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {
        
        int length = timePoints.size();
        unordered_set<string> se(timePoints.begin(), timePoints.end());
        if (se.size() < length) {
            return 0;
        }

        std::function<int(string, string)> calculate_diff = [](string t1, string t2) {
            int hours = stoi(t2.substr(0, 2)) - stoi(t1.substr(0, 2));
            int minutes = stoi(t2.substr(3, 2)) - stoi(t1.substr(3, 2));
            minutes += hours * 60;
            return min(minutes, 60*24 - minutes);
        };

        std::sort(timePoints.begin(), timePoints.end());
        int mindiff = calculate_diff(timePoints[0], timePoints.back());
        for (int i = 1; i < length; ++i) {
            mindiff = min(mindiff, calculate_diff(timePoints[i-1], timePoints[i]));
        }
        return mindiff;
    }
};

/*
https://leetcode-cn.com/submissions/detail/259634329/

执行用时：8 ms, 在所有 C++ 提交中击败了91.06%的用户
内存消耗：13.7 MB, 在所有 C++ 提交中击败了9.12%的用户
通过测试用例：
113 / 113
*/
