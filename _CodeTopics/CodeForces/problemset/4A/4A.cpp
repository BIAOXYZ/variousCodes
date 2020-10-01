#include <iostream>

int main(){
    int weight = 0;
    std::cin >> weight;
    std::string output = (weight <= 2 || weight % 2) ? "NO" : "YES";
    std::cout << output << std::endl;
    return 0;
}

/*
https://codeforces.com/problemset/submission/4/94371805
*/
