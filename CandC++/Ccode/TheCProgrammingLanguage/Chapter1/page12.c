#include <stdio.h>

/* 对 fahr = 0, 20, ..., 300; 打印华氏
   温度到摄氏温度的对应表。——浮点数版本 */
main()
{
    float fahr, celsius;
    int lower, upper, step;

    lower = 0;      /* 温度表的下限 */
    upper = 300;    /* 温度表的上限 */
    step = 20;      /* 温度增长步幅 */

    fahr = lower;
    while (fahr <= upper) {
        celsius = (5.0/9.0) * (fahr-32.0);
        printf("%3.0f %6.1f\n", fahr, celsius);
        fahr = fahr + step;
    }
}
