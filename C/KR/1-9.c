#include <stdio.h>

int main(int argc, const char *argv[])
{
    char c,d;
    for(;;)
    {
        c = getchar();
        if(c  == ' ')
        {
            while ((d = getchar()) == ' ') 
            {
                continue;
            }
        }
        putchar(c);
        if( c == ' ')
        {
            putchar(d);
        }
    }
    return 0;
}

/*
 FIXME:
 now how to merge the two
    
      if(c  == ' ')

into one ?
*/
