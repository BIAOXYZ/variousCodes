#include <stdio.h>

/* ��ϰ 1-4. ��дһ�����򣬴�ӡ�������¶ȵ������¶ȵĶ��ձ� */
main()
{
    float celsius, fahr;
    int lower, upper, step;

    lower = 0;      /* �¶ȱ������ */
    upper = 300;    /* �¶ȱ������ */
    step = 20;      /* �¶��������� */

    fahr = lower;
    while (fahr <= upper) {
        celsius = (5.0/9.0) * (fahr-32.0);
        printf("%6.1f %3.0f\n", celsius, fahr);
        fahr = fahr + step;
    }
}
