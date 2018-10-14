#include <stdio.h>

/* 练习 1-4. 编写一个程序，打印出摄氏温度到华氏温度的对照表。 */
main()
{
    float celsius, fahr;
    int lower, upper, step;

    lower = 0;      /* 温度表的下限 */
    upper = 300;    /* 温度表的上限 */
    step = 20;      /* 温度增长步幅 */

    fahr = lower;
    while (fahr <= upper) {
        celsius = (5.0/9.0) * (fahr-32.0);
        printf("%6.1f %3.0f\n", celsius, fahr);
        fahr = fahr + step;
    }
}
