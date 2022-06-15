#include <stdio.h>
#include <math.h>
#include <string.h>

void datatype(){
    char var1 = 'S';
    char var2 []= "Operating system";
    //long long a = 20101073;
    printf("the course name is: %s \n",var2);
}

float summation(float a, float b){
    int c;
    c = a+b;
    return c;
}
float arithmetic_function(){
    float a,b;
    scanf("%f",&a);
    scanf("%f",&b);
    float d = summation(a,b);
    int var1 = pow(2,3);
    int var2 = pow(4,3);
    printf("Summation-> %2f \n",d);
    printf("powered variables: %d ,%d",var1,var2);
    return d;
}
int multiarray(){
    int simple[5] = {1,2,3,4,5};
    int complex[3][2] = {
        {1,2}, {2,3}, {3,4}
    };
    
}

void string(){
    //char s1 [] ={'h','e','l','l','o'};
    char s1[] = {'H','e','l','l','o','\0'};
    char s2[] = " world";
    printf("%s",strcat(s1,s2));
}
void unstring(){
    char test1,test2,test3;
    printf("type single character: ");
    scanf("%c",&test1);
    printf("\nYou typed: %c \n",test1);
    getchar();
    printf("type single character: ");
    scanf("%c",&test2);
    printf("\nYou typed: %c \n",test2);
}

int main(){
    //datatype();
    //arithmetic_function();
    //multiarray();
    string();
    return 0;
}
