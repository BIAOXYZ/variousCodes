#include <stdio.h>

/* 练习 1-3. 修改温度转换程序，在输出的转换表前加一个标题。 */
main()
{
    float fahr, celsius;
    int lower, upper, step;

    lower = 0;      /* 温度表的下限 */
    upper = 300;    /* 温度表的上限 */
    step = 20;      /* 温度增长步幅 */

    fahr = lower;

    printf("This is the heading for the temperature conversion table:\n");

    while (fahr <= upper) {
        celsius = (5.0/9.0) * (fahr-32.0);
        printf("%3.0f %6.1f\n", fahr, celsius);
        fahr = fahr + step;
    }
}
