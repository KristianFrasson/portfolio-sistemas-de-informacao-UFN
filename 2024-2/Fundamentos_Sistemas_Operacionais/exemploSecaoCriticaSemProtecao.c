#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

#define N 100000000
int num = 0;
pthread_mutex_t mutex;

void* contaIteracoes(void* nome){
    int aux, i;

    for(i = 0; i < N; i++) {
        pthread_mutex_lock(&mutex);
        aux = num;
        aux = aux + 1;
        num = aux;
        pthread_mutex_unlock(&mutex);
    }

    pthread_exit(0);
}

int main(){
    int i;
    pthread_t thUm, thDois;

    pthread_mutex_init(&mutex, NULL);

    pthread_create(&thUm, 0, contaIteracoes, "Um");
    pthread_create(&thDois, 0, contaIteracoes, "Dois");
    
    pthread_join(thUm, NULL);
    pthread_join(thDois, NULL);

    if(num != 2 * N)
        printf("**** ERRO na SOMA TOTAL das iteracoees dos Threads ****\nnum = %d\n", num);
    else
        printf("OK! SOMA FINAL CORRETA!!!\nnum = 2 * N = %d\n", num);
    printf("Fim do Thread Principal\n");

    pthread_mutex_destroy(&mutex);
    return 1;
}