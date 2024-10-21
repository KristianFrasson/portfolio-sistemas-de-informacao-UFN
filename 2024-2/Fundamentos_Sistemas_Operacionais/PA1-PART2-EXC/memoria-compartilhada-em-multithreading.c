#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

// Variável global compartilhada entre as threads
int shared_data = 0;

// Mutex para proteger o acesso à variável compartilhada
pthread_mutex_t lock;

// Função que será executada pelas threads
void* increment(void* arg) {
    // Tenta bloquear o mutex antes de acessar a variável compartilhada
    if (pthread_mutex_lock(&lock) != 0) {
        perror("pthread_mutex_lock");
        return NULL;
    }

    // Incrementa a variável compartilhada
    shared_data++;
    printf("Valor compartilhado: %d\n", shared_data);

    // Desbloqueia o mutex após acessar a variável compartilhada
    if (pthread_mutex_unlock(&lock) != 0) {
        perror("pthread_mutex_unlock");
        return NULL;
    }

    return NULL;
}

int main() {
    // Identificadores das threads
    pthread_t t1, t2;

    // Inicializa o mutex antes de criar as threads
    if (pthread_mutex_init(&lock, NULL) != 0) {
        perror("pthread_mutex_init");
        return 1;
    }

    // Cria a primeira thread e verifica se houve erro
    if (pthread_create(&t1, NULL, increment, NULL) != 0) {
        perror("pthread_create t1");
        pthread_mutex_destroy(&lock);
        return 1;
    }

    // Cria a segunda thread e verifica se houve erro
    if (pthread_create(&t2, NULL, increment, NULL) != 0) {
        perror("pthread_create t2");
        pthread_mutex_destroy(&lock);
        return 1;
    }

    // Espera a primeira thread terminar e verifica se houve erro
    if (pthread_join(t1, NULL) != 0) {
        perror("pthread_join t1");
        pthread_mutex_destroy(&lock);
        return 1;
    }

    // Espera a segunda thread terminar e verifica se houve erro
    if (pthread_join(t2, NULL) != 0) {
        perror("pthread_join t2");
        pthread_mutex_destroy(&lock);
        return 1;
    }

    // Destroi o mutex após o uso
    if (pthread_mutex_destroy(&lock) != 0) {
        perror("pthread_mutex_destroy");
        return 1;
    }

    return 0;
}