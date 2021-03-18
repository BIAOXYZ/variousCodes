class ParkingSystem {
private:
    vector<int> capability;
    // error: expected parameter declarator
    // 初始化时如果编译器会分不清是类成员还是类函数。。。所以不能写成： 
    //   vector<int> park(3, 0);
    // 而是要这么写成下面这样：
    vector<int> park = vector<int>(3, 0);
public:
    ParkingSystem(int big, int medium, int small) {
        capability = {big, medium, small};
    }
    
    bool addCar(int carType) {
        if (park[carType-1] < capability[carType-1]) {
            park[carType-1]++;
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
https://leetcode-cn.com/submissions/detail/156970063/

102 / 102 个通过测试用例
状态：通过
执行用时: 56 ms
内存消耗: 32.3 MB

执行用时：56 ms, 在所有 C++ 提交中击败了97.61%的用户
内存消耗：32.3 MB, 在所有 C++ 提交中击败了49.60%的用户
*/
