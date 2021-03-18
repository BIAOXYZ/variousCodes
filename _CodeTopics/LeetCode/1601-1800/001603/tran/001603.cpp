class ParkingSystem {
private:
    list<int> capability;
    list<int> park;
public:
    ParkingSystem(int big, int medium, int small) {
        capability = {big, medium, small};
        park = {0, 0, 0};
    }
    
    bool addCar(int carType) {
        std::list<int>::iterator it = park.begin(), it2 = capability.begin();
        for (int i = 0; i < carType - 1; ++i) {
            ++it++;
            ++it2;
        }
        if (*it < *it2) {
            // 这里用 *it++ 是不行的。
            (*it)++;
            return true;
        }
        return false;
    }
};

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem* obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj->addCar(carType);
 */
 
/*
https://leetcode-cn.com/submissions/detail/156968902/

102 / 102 个通过测试用例
状态：通过
执行用时: 72 ms
内存消耗: 32.3 MB

执行用时：72 ms, 在所有 C++ 提交中击败了64.51%的用户
内存消耗：32.3 MB, 在所有 C++ 提交中击败了58.55%的用户
*/
