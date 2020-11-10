#include <stdio.h>

void swap1(int x, int y) {
    int tmp;
    tmp = x; x = y; y = tmp;
    return;
}
void swap2(int* x, int *y) {
    int tmp;
    tmp = *x; *x = *y; *y = tmp;
    return;
}

int main()
{

    int a = 1, b = 2;
    swap1(a, b);
    printf("If you use value as argument, swap1() is NOT in effect: %d, %d\n", a, b);
    
    int c = 3, d = 4;
    swap2(&c, &d);
    printf("If you use pointer/address as argument, swap2() is in effect: %d, %d\n", c, d);
    return 0;
}

/******************************************************************************
If you use value as argument, swap1() is NOT in effect: 1, 2                                                          
If you use pointer/address as argument, swap2() is in effect: 4, 3
*******************************************************************************/
