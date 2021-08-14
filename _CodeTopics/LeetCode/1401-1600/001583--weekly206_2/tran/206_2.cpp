class Solution {
public:
    int unhappyFriends(int n, vector<vector<int>>& preferences, vector<vector<int>>& pairs) {

        // 第 206 场周赛第二题。原始提交链接为：
        // https://leetcode-cn.com/submissions/detail/107523794/

        int length = pairs.size();
        unordered_map<int, int> dic = unordered_map<int, int>{};
        for (int i = 0; i < length; ++i) {
            dic[pairs[i][0]] = i;
            dic[pairs[i][1]] = i;
        }

        vector<int> unhappy = vector<int>{};
        function<void(vector<int>&)> deal_with_pair = [&](vector<int>& pair) -> void {
            for (int ind : vector<int>{0, 1}) {
                if (find(unhappy.begin(), unhappy.end(), pair[ind]) != unhappy.end()) {
                    continue;
                }
                vector<int> tmplist = preferences[pair[ind]];
                int pos = find(tmplist.begin(), tmplist.end(), pair[1-ind]) - tmplist.begin();
                for (int peopleInd = 0; peopleInd < pos; ++peopleInd) {
                    int people = tmplist[peopleInd];
                    vector<int> anotherPair = pairs[dic[people]];
                    int anotherPeople;
                    if (people == anotherPair[0]) {
                        anotherPeople = anotherPair[1];
                    } else {
                        anotherPeople = anotherPair[0];
                    }
                    vector<int> anotherList = preferences[people];
                    int pos2 = find(anotherList.begin(), anotherList.end(), anotherPeople) - anotherList.begin();
                    int pos3 = find(anotherList.begin(), anotherList.end(), pair[ind]) - anotherList.begin();
                    if (pos2 > pos3) {
                        if (find(unhappy.begin(), unhappy.end(), pair[ind]) == unhappy.end()) {
                            unhappy.push_back(pair[ind]);
                        }
                        if (find(unhappy.begin(), unhappy.end(), people) == unhappy.end()) {
                            unhappy.push_back(people);
                        }                        
                    }
                }
            }
        };

        for (auto& pair : pairs)
            deal_with_pair(pair);

        return unhappy.size();
    }
};

/*
https://leetcode-cn.com/submissions/detail/206934162/

99 / 99 个通过测试用例
状态：通过
执行用时: 64 ms
内存消耗: 40.5 MB

执行用时：64 ms, 在所有 C++ 提交中击败了68.33%的用户
内存消耗：40.5 MB, 在所有 C++ 提交中击败了21.67%的用户
*/
