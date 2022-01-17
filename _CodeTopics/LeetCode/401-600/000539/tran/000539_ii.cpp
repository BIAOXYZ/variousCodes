class Solution {
    // 一般就算不用 lambda 匿名函数，也是把这种自己定义的函数写在 public: 下的，
    // 这次的答案是我第一次见到写在这个位置的 —— 于是就把自己上一个写法的也这么写试试。
    // 此外答案里还涉及到了 C++ 的 <climits> 库里的 INT_MAX，但是我这里因为细微区别，不涉及。
    int calculate_diff(string t1, string t2) {
        int hours = stoi(t2.substr(0, 2)) - stoi(t1.substr(0, 2));
        int minutes = stoi(t2.substr(3, 2)) - stoi(t1.substr(3, 2));
        minutes += hours * 60;
        //// return min(minutes, 60*24 - minutes);
        //// 这里用条件表达式代替下 min。
        return minutes < 60*24 - minutes ? minutes : 60*24 - minutes;
    };
public:
    int findMinDifference(vector<string>& timePoints) {

        int length = timePoints.size();
        unordered_set<string> se(timePoints.begin(), timePoints.end());
        if (se.size() < length) {
            return 0;
        }

        std::sort(timePoints.begin(), timePoints.end());
        int mindiff = calculate_diff(timePoints[0], timePoints.back());
        for (int i = 1; i < length; ++i) {
            mindiff = min(mindiff, calculate_diff(timePoints[i-1], timePoints[i]));
        }
        return mindiff;
    }
};

/*
https://leetcode-cn.com/submissions/detail/259634686/

执行用时：8 ms, 在所有 C++ 提交中击败了91.06%的用户
内存消耗：13.8 MB, 在所有 C++ 提交中击败了5.01%的用户
通过测试用例：
113 / 113
*/
