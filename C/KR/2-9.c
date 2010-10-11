#include <stdio.h>

int main(int argc, const char *argv[])
{
    int x = 7;
    int b = 0;
    while (x != 0) 
    {
        x &= x -1;
        b++;
    }
    printf("%d\n", b);
    return 0;
}
