#include <stdio.h>

int main(int argc, const char *argv[])
{
    int i;
    char s[10];
    for (i = 0; s[i] != 3; i++) 
    {
        s[i] = i;
    }
    return 0;
}

/*
 * the above code won't stop when s[1] == 3 as I wanted, later when I add some
 * test code: 
 *
 *      for(i = 0; printf("%d\n", s[i]), s[i] != 3; i++)
 *      
 * and I realized before the code block inside "{}" of this for loop, s[i] is
 * junk data, but if you add code inside the block or after the block the s[i]
 * all turned out to be right  
 *
 * So, the lesson is: never use for loop like above!
