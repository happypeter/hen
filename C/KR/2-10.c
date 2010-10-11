#include <stdio.h>

int lower( int );
int main(int argc, const char *argv[])
{
    int c = 'A';
    printf("%c\n", lower(c));
    return 0;
}
int lower( int d )
{
    return (d >= 'A' && d <= 'Z')?(d + 'a' - 'A'):d;
}
