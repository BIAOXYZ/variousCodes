#if 0

/* bitcount��ͳ�� x ��Ϊ 1 �ı���λ */
int bitcount(unsigned x)
{
    int b;

    for (b = 0; x != 0; x >>= 1)
        if (x & 01)
            b++;
    return b;
}

#endif // 0

/* bitcount��ͳ�� x ��Ϊ 1 �ı���λ */
int bitcount(unsigned x)
{
    int b;

    for (b = 0; x != 0; x >>= 1)
        if (x & 01)
            b++;
    return b;
}
