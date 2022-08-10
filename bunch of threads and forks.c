#include<stdio.h>
#include <stdbool.h>
#include<string.h>
#include<stdlib.h>
char ch[100];
int main(int args,char *arg[])
{
    FILE *file;
    int i=0;
    file=fopen(arg[1],"w");
    char ch[100];
    scanf("%s",ch);
    while (true)
    {
        
        bool check=true;
        for(int i=0;i<strlen(ch)-1;i++)
        {
            if(ch[i]=='-' && ch[i+1]=='1')
                {
                    check=false;
                    break;
                }
        }
        if(check==false)
            break;
        fprintf(file,"%s\n",ch);
        scanf("%s",ch);
    }
    fclose(file);
    return 0;  


}


#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
  
int main()
{
    int parent,child,grandchild;
    child=fork();
    if(child==0)
    {
        
        grandchild=fork();
        if(grandchild==0)
        {
            printf("I am grandchild\n");
            
        }
        else
        {
            sleep(1);
            printf("I am child\n");
        }
    }
    else
    {
        sleep(3);
        printf("I am parent\n");
    }
    
}

#include<stdio.h>
#include <stdlib.h>
#include <unistd.h>
int main(int argc, char *argv[])
{
    int n=argc-2;
    
    int arr[n];
    for(int i=0;i<n;i++)
       arr[i]=atoi(argv[i+2]);
    int child;
    child=fork();
    if(child==0)
    {
        printf("Sorted Array\n");
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n-i-1;j++)
            {
                if(arr[j]<arr[j+1])
                {
                    int temp=arr[j];
                    arr[j]=arr[j+1];
                    arr[j+1]=temp;
                }
            }
        }
        for(int i=0;i<n;i++)
            printf("%d ",arr[i]);
        printf("\n");
    }
    else
    {
        sleep(3);
        printf("Even/Odd Status\n");
        for(int i=0;i<n;i++)
        {
            if(arr[i]%2==0)
                printf("%d ---> Even\n",arr[i]);
            else
                printf("%d ---> Odd\n",arr[i]);
        }
    }
    

}

#include<stdio.h>
#include <stdlib.h>
#include <unistd.h>
int main()
{
    int ppid,cpid;
    int ppidno,cpidno,gpid1no,gpid2no,gpid3no;
    ppid=fork();
    if(ppid==0)
    {
       cpid=fork();
       if(cpid==0)
       {
            gpid1no=getpid();
            gpid2no=getpid();
            gpid3no=getpid();
            

       }
       else
       {
           sleep(2);
           cpidno=getpid();
       }
    }
    else
    {
        sleep(3);
        ppidno=getpid();
        printf("1. Parent process ID : %d\n",ppidno);
        printf("2. Child process ID : %d\n",cpidno);
        printf("3. Grand Child process ID : %d\n",gpid1no);
        printf("4. Grand Child process ID : %d\n",gpid2no);
        printf("5. Grand Child process ID : %d\n",gpid3no);
    }
    
}

#include<stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include<pthread.h>

//gcc Task8.c -o Task8 -pthread


void* open(void* p)
{
    printf("thread-%d closing\n",* (int*)p);
    pthread_exit(NULL);
    
}
int main()
{
    pthread_t id[5];
    for(int i=1;i<=5;i++)
    {
        printf("thread-%d running\n",i);
        pthread_create(&id[i],NULL,open,&i);
        int* ptr;
        pthread_join(id[i],(void**)&ptr);
    }
    return 0;
}

#include<stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include<pthread.h>
int count=1;
void* open(void* p)
{
    for(int i=1;i<=5;i++)
    {
        printf("thread-%d prints %d\n",* (int*)p+1,count);
        count++;
    }
    pthread_exit(NULL);
    


}
int main()
{
    pthread_t id[5];
    for(int i=0;i<5;i++)
    {
        
        pthread_create(&id[i],NULL,open,&i);
        int* ptr;
        pthread_join(id[i],(void**)&ptr);
    }
    return 0;
}


#include<stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include<pthread.h>
#include<string.h>
void *cASCII(void *str1)
{
    char* str=(char*)str1;
    int *n=malloc(sizeof(int));
    int sum=0;
    for(int i=0;i<strlen(str);i++)
    {
        sum+=str[i];
    }
    *n=sum;
    return (void*)n;
    pthread_exit(NULL);
}

int main()
{
    char name1[1000],name2[1000],name3[1000];
    scanf("%s %s %s",name1,name2,name3);
    pthread_t ptd1,ptd2,ptd3;
    pthread_create(&ptd1,NULL,cASCII,name1);
    int *ptr1;
    pthread_join(ptd1,(void**)&ptr1);
    pthread_create(&ptd2,NULL,cASCII,name2);
    int *ptr2;
    pthread_join(ptd2,(void**)&ptr2);
    pthread_create(&ptd3,NULL,cASCII,name3);
    int *ptr3;
    pthread_join(ptd3,(void**)&ptr3);

    if(*ptr1==*ptr2 && *ptr1==*ptr3)
        printf("Youreka\n");
    else if(*ptr1==*ptr2 || *ptr1==*ptr3 || *ptr3==*ptr2)
        printf("Miracle\n");
    else
        printf("Hasta la vista\n");

}
