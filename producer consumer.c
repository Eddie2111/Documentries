#include <pthread.h>   

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX 10
#define BUFLEN 6
#define MAX_COUNT 15
#define NUMTHREAD 2      /* number of threads */

void * consumer(int *id);
void * producer(int *id);

char buffer[BUFLEN];
char source[BUFLEN];
int pCount = 0;
int cCount = 0;
int buflen;
// initialize pthread mutex and condition variables
pthread_mutex_t count_mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t nonEmpty  = PTHREAD_COND_INITIALIZER;
pthread_cond_t full  = PTHREAD_COND_INITIALIZER;
int thread_id[NUMTHREAD]  = {0,1};

int i = 0;
int j = 0; 

int main(){
  int i;
  /* define the type to be pthread */
  pthread_t thread[NUMTHREAD];

  strcpy(source,"abcdef");
  buflen = strlen(source);
  /* create 2 threads*/
  /* create one consumer and one producer */
  pthread_create(&thread[0], NULL, (void *)consumer, &thread_id[0]); //thread 0
  pthread_create(&thread[1], NULL, (void *)producer, &thread_id[1]); //thread 1
    /* waiting for the threads to finish */
  for(i=0; i< NUMTHREAD ; i++)
    {
      pthread_join(thread[i], NULL);
    }
}

void * consumer(int *id)
{
  /* lock the variable */
  pthread_mutex_lock(&count_mutex);

  while(j < MAX)
    {
      /* buffer needs to recieve */
      pthread_cond_wait(&nonEmpty, &count_mutex);

      /* incrementing counter */
      printf("%d consumed %c: by Thread %d\n",j, buffer[cCount], *id);
      cCount = (cCount + 1) % BUFLEN;
      fflush(stdout);
      j ++;
      if (j < (MAX - 2))     
	if (rand()%100 < 30)
	  sleep(rand()%3);
    }
  /*unlocking variable after consumption*/
  pthread_mutex_unlock(&count_mutex);
}

void * producer(int *id)
{

  while (i < MAX)
    {
      /* lock the variable */
      pthread_mutex_lock(&count_mutex);
      strcpy(buffer,"");
      buffer[pCount] = source[pCount%buflen];
      printf("%d produced %c: by Thread %d\n",i, buffer[pCount], *id);
      fflush(stdout);
      pCount = (pCount + 1) % BUFLEN;
      i ++;
      pthread_cond_signal(&nonEmpty);
      /*unlock the variable*/
      pthread_mutex_unlock(&count_mutex);
      if (i < (MAX - 2))     
	  if (rand()%100 >= 30) sleep(rand()%3);
    }
}
