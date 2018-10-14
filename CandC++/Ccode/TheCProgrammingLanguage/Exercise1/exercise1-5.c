/* 练习 1-5. 修改温度转换程序，以相反的顺序打印温度对应表，即从 300°F 到 0°F。 */

# include <stdio.h>

main()
{
    int fahr;
    for (fahr = 300; fahr >= 0; fahr-=20)
        printf("%10d,%.1f\n", fahr, (5.0/9.0)*(fahr-32)); //如果第一个格式控制只有%d，第一排fahr是无法右对齐的。更奇怪的是写成%1.5d，还会补一些0
}
