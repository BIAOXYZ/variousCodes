#include <stdio.h>

void double_num(int x) {
    x = x * 2;
    return;
}
void ptr_double_num(int* x) {
    *x = *x * 2;
    return;
}

int main()
{

    int a = 3, b = 3;
    double_num(a);
    printf("After double operation without pointer, a is: %d\n", a);
    ptr_double_num(&b);
    printf("After double operation with pointer, b is: %d\n", b);
    return 0;
}

/******************************************************************************
After double operation without pointer, a is: 3                                                                       
After double operation with pointer, b is: 6
*******************************************************************************/
