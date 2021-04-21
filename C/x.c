#include <stdio.h>



void pp(float *arr0,float *arr1,float *arr2,float *arr3){
	int i;
    for ( i = 0; i < 10; i++ )
        { 
            arr0[ i ] = 2.560; /* 设置元素 i 为 i + 100 */
        }
	
}

//gcc -shared -m64 -o x.dll x.c
