
#include <stdlib.h>

void getdata(int* pa,int* pb,int* pc);
int quad(int a,int b,int c,double* proot1,double* proot2);
void printresults(int numroots,int a,int b,int c,double root1,double root2)\


int main(void){
  int a,b,c;
  double root1,root2;
  char again ='Y';
  printf("solve");
  while(again=='Y' || again=='y'){
      getdata(&a,&b,&c);
      numroots=quad(a,b,c,&root1,&root2);
}}