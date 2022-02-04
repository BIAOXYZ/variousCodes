class Solution {
public:
    int countGoodRectangles(vector<vector<int>>& rectangles) {
        
        // 第 224 场周赛第一题
        // https://leetcode-cn.com/submissions/detail/139008247/

        unordered_map<int, int> dic;
        // 当然也可以用 auto 或者 auto&： `for (auto rectangle : rectangles) {`
        for (const vector<int>& rectangle : rectangles) {
            int key = min(rectangle[0], rectangle[1]);
            if (dic.find(key) != dic.end()) {
                ++dic[key];
            } else {
                dic[key] = 1;
            }
        }
        vector<int> keys;
        for (const auto & [k, v] : dic) {
            keys.push_back(k);
        }
        int maxKey = *max_element(keys.begin(), keys.end());
        return dic[maxKey];
    }
};

/*
https://leetcode-cn.com/submissions/detail/264682729/

执行用时：40 ms, 在所有 C++ 提交中击败了54.13%的用户
内存消耗：18 MB, 在所有 C++ 提交中击败了55.05%的用户
通过测试用例：
68 / 68
*/
