class AuthenticationManager {
    
    // 第 48 场双周赛第二题
    // https://leetcode.cn/submissions/detail/157686015/

private:
    unordered_map<string, int> _mp;
    int _live;

public:
    AuthenticationManager(int timeToLive) {
        _mp = unordered_map<string, int>{};
        _live = timeToLive;
    }
    
    void generate(string tokenId, int currentTime) {
        _mp[tokenId] = currentTime + _live;
    }
    
    void renew(string tokenId, int currentTime) {
        if (_mp.find(tokenId) != _mp.end() && currentTime < _mp[tokenId]) {
            _mp[tokenId] = currentTime + _live;
        }
    }
    
    int countUnexpiredTokens(int currentTime) {
        int res = 0;
        for (auto [k, v] : _mp) {
            if (currentTime < v) {
                res += 1;
            }
        }
        return res;
    }
};

/**
 * Your AuthenticationManager object will be instantiated and called as such:
 * AuthenticationManager* obj = new AuthenticationManager(timeToLive);
 * obj->generate(tokenId,currentTime);
 * obj->renew(tokenId,currentTime);
 * int param_3 = obj->countUnexpiredTokens(currentTime);
 */

/*
https://leetcode.cn/submissions/detail/400750982/

执行用时：
120 ms
, 在所有 C++ 提交中击败了
23.83%
的用户
内存消耗：
29.5 MB
, 在所有 C++ 提交中击败了
40.65%
的用户
通过测试用例：
90 / 90
*/
