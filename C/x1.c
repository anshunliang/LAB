#include <stdio.h>



void pp(float *arr0,float *arr1,float *arr2,float *arr3,float *arr4,float *arr5,int x){
	int i;
    float j,k,l,m,n;

    for ( i = 0; i < x; i++ )
        { 
            j=arr2[i]-arr1[i];   //原始范围
            k=arr0[i]-arr1[i];   //原始差值
            l=k/j;               //工程值的百分比
            m=l*(arr4[i]-arr3[i]);
            arr5[i]=m+arr3[i];
        }
	
}

//gcc -shared -m64 -o x.dll x.c
