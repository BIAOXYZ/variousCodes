#include <stdio.h>

/* 按 fahr = 0, 20, ..., 300
   打印华氏温度-摄氏温度对应表 */
main()
{
    int fahr, celsius;
    int lower, upper, step;

    lower = 0;      /* 温度表的下限 */
    upper = 300;    /* 温度表的上限 */
    step = 20;      /* 温度增长步幅 */

    fahr = lower;
    while (fahr <= upper) {
        celsius = 5 * (fahr-32) / 9;
        printf("%d\t%d\n", fahr, celsius);
        fahr = fahr + step;
    }
}
