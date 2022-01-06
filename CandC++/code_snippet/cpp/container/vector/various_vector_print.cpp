#include <iostream>
#include <vector>
using namespace std;


// for print the whole vector
#include <iterator>
template <typename T>
std::ostream& operator<< (std::ostream& out, const std::vector<T>& v) {
    if ( !v.empty() ) {
        out << '[';
        std::copy (v.begin(), v.end(), std::ostream_iterator<T>(out, ", "));
        out << "\b\b]";
    }
    return out;
}


int main(void){

    std::vector<int> vec = {1,2,3,4,5};
    
    for (int i = 0; i < vec.size(); ++i) {
        std::cout << vec[i] << ", ";
    }
    std::cout << std::endl;
    
    for (auto i = 0; i < vec.size(); ++i) {
        std::cout << vec[i] << ", ";
    }
    std::cout << std::endl;
    
    std::cout << "------------------------------" << std::endl;
    
    for (auto it = vec.begin(); it != vec.end(); ++it) {
        std::cout << *it << ", ";
    }
    std::cout << std::endl;
    
    for (std::vector<int>::iterator it = vec.begin(); it != vec.end(); ++it) {
        std::cout << *it << ", ";
    }
    std::cout << std::endl;
    
    std::cout << "------------------------------" << std::endl;
    
    for (auto elem : vec) {
        std::cout << elem << ", ";
    }
    std::cout << std::endl;
    
    for (int elem : vec) {
        std::cout << elem << ", ";
    }
    std::cout << std::endl;
    
    std::cout << "------------------------------" << std::endl;
    
    // see the template above
    std::cout << vec << std::endl;
    
}

/*
1, 2, 3, 4, 5, 
1, 2, 3, 4, 5, 
------------------------------
1, 2, 3, 4, 5, 
1, 2, 3, 4, 5, 
------------------------------
1, 2, 3, 4, 5, 
1, 2, 3, 4, 5, 
------------------------------
[1, 2, 3, 4, 5, ]
*/
