#include <stdio.h>

#define LOWER 0     /* �¶ȱ������ */
#define UPPER 300   /* �¶ȱ������ */
#define STEP 20     /* ���� */

/* ��ӡ����-�����¶ȶ��ձ� */
main()
{
    int fahr;

    for (fahr = LOWER; fahr <= UPPER; fahr = fahr + STEP)
        printf("%3d %6.1f\n", fahr, (5.0/9.0)*(fahr-32));
}
