#include <iostream>
#include <vector>
using namespace std;

int main() {
    
    vector<int> vec {1,2,3,4,5,6,7,8,9,10};
    cout << "修改前" << endl;
    for (auto n : vec)
	    std::cout << n++;
 
    cout << endl;
    
    cout << "修改后" << endl;
    for (auto j : vec)
	    std::cout << j;
    
    return 0;
}

/******************************************************************************
修改前
12345678910
修改后
12345678910
*******************************************************************************/
