#include <stdio.h>

/* ��ϰ 1-3. �޸��¶�ת�������������ת����ǰ��һ�����⡣ */
main()
{
    float fahr, celsius;
    int lower, upper, step;

    lower = 0;      /* �¶ȱ������ */
    upper = 300;    /* �¶ȱ������ */
    step = 20;      /* �¶��������� */

    fahr = lower;

    printf("This is the heading for the temperature conversion table:\n");

    while (fahr <= upper) {
        celsius = (5.0/9.0) * (fahr-32.0);
        printf("%3.0f %6.1f\n", fahr, celsius);
        fahr = fahr + step;
    }
}
