#define MAXVAL 100  /* ջ val �������� */

int sp = 0;         /* ջ����һ������λ��*/
double val[MAXVAL]; /* ���ֵ��ջ */

/* push���� f ѹ��ջ�� */
void push(double f)
{
    if (sp < MAXVAL)
        val[sp++] = f;
    else
        printf ("error: ջ�������ܽ�%g ѹջ\n", f);
}

/* pop������������ջ����ֵ */
void pop(void)
{
    if (sp > 0)
        return val[--sp];
    else {
        printf ("error: ջ��\n");
        return 0.0;
    }
}
