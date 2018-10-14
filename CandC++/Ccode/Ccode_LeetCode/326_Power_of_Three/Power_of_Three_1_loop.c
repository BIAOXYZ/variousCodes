bool isPowerOfThree(int n) {

    if (n == 1 || n == 3)
        return true;
    if (n == 0 || n == 2)
        return false;

    for ( ; n > 3 && (n % 3 == 0) ; n = n/3)
        ;
    if (n == 3)
        return true;
    else
        return false;
}
