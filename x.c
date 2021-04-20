#include <stdio.h>



void pp(int *arr){
	int i;
    for ( i = 0; i < 10; i++ )
        { 
            arr[ i ] = i*20; /* 设置元素 i 为 i + 100 */
        }
	
}

//gcc -shared -o x.dll x.c
