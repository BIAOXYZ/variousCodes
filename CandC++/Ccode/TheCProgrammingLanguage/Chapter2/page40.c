#if 0

/* getbits����ȡ��λ�� p ��ʼ�� n ������λ */
unsigned getbits(unsigned x, int p, int n)
{
    return (x >> (p+1-n)) & ~(~0 << n);
}

#endif // 0


/* getbits����ȡ��λ�� p ��ʼ�� n ������λ */
unsigned getbits(unsigned x, int p, int n)
{
    return (x >> (p+1-n)) & ~(~0 << n);
}
