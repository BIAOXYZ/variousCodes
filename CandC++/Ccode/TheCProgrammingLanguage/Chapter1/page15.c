#include <stdio.h>

/* 将输入拷贝到输出；版本 1 */
main()
{
    int c;
    c = getchar();
    while (c != EOF) {
        putchar(c);
        c = getchar();
    }
}
