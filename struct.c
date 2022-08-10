#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <string.h>
int main()
{
    struct Person {
      char name[50];
      int citNo;
      float salary;
    };

    struct Person person1,person2,person3,p[20];
    char c[20];
    strcpy(c,"blake hazard!");
    strcpy(person1.name, "George Orwell");
    strcpy(person2.name,"halliday");
    person1.salary = 34.200;
    printf("%s %s",person1.name,c);
    for (int i = 0 ; i <16; i++){
        printf("%c\n",person1.name[i]);
    }
    return 0;
}
