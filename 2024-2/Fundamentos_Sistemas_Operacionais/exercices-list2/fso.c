// 1. Programa com Dois Processos: Cálculo da Área e Perímetro
// Este programa cria dois processos. O processo pai calcula o perímetro de um terreno retangular, enquanto o processo filho calcula a área.

#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    float largura, comprimento;
    printf("Informe a largura do terreno: ");
    scanf("%f", &largura);
    printf("Informe o comprimento do terreno: ");
    scanf("%f", &comprimento);

    pid_t pid = fork();

    if (pid == 0) { 
        // Processo Filho - Calcula a área
        float area = largura * comprimento;
        printf("Filho: A área do terreno é: %.2f\n", area);
    } else {
        // Processo Pai - Calcula o perímetro
        wait(NULL); // Aguarda o processo filho terminar
        float perimetro = 2 * (largura + comprimento);
        printf("Pai: O perímetro do terreno é: %.2f\n", perimetro);
    }

    return 0;
}

// 2. Programa com 3 Processos Concorrentes
// Neste programa, 3 processos imprimem sua identificação em um laço de repetição. O comportamento do escalonamento será visível na ordem das execuções.

#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    int N;
    printf("Informe o número de interações: ");
    scanf("%d", &N);

    for (int i = 0; i < 3; i++) {
        if (fork() == 0) {
            // Processos filhos
            for (int j = 0; j < N; j++) {
                printf("Processo %d: Iteração %d\n", getpid(), j+1);
                sleep(1); // Adiciona uma pausa para visualizar o escalonamento
            }
            return 0; // Finaliza o processo filho
        }
    }
    
    // Processo Pai aguarda os filhos
    for (int i = 0; i < 3; i++) {
        wait(NULL);
    }

    return 0;
}

// 3. Programa com Pai e Dois Filhos
// Este programa cria um processo pai e dois processos filhos que imprimem números em diferentes intervalos de tempo.

#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

void filho1() {
    for (int i = 100; i <= 200; i++) {
        printf("Filho1: %d\n", i);
        sleep(1);
    }
    printf("Filho1 finalizou.\n");
}

void filho2() {
    for (int i = 250; i <= 350; i++) {
        printf("Filho2: %d\n", i);
        sleep(1);
    }
    printf("Filho2 finalizou.\n");
}

void pai() {
    for (int i = 1; i <= 50; i++) {
        printf("Pai: %d\n", i);
        sleep(2);
    }
    printf("Pai finalizou.\n");
}

int main() {
    pid_t pid1 = fork();

    if (pid1 == 0) {
        filho1();
    } else {
        pid_t pid2 = fork();
        if (pid2 == 0) {
            filho2();
        } else {
            pai();
            wait(NULL);  // Aguarda os filhos finalizarem
            wait(NULL);
        }
    }

    return 0;
}

// 4. Algoritmo de Árvore de Processos
// Este programa cria uma árvore de processos com um pai e cinco filhos
// onde três filhos são diretos do pai, e os outros dois são filhos de um dos filhos.

#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    pid_t filho1, filho2, filho3, filho4, filho5;

    filho1 = fork();
    if (filho1 == 0) {
        printf("Filho 1 criado\n");
        filho4 = fork();
        if (filho4 == 0) {
            printf("Filho 4 criado\n");
            return 0;
        }
        wait(NULL); // Filho 1 espera Filho 4
        return 0;
    }

    filho2 = fork();
    if (filho2 == 0) {
        printf("Filho 2 criado\n");
        filho5 = fork();
        if (filho5 == 0) {
            printf("Filho 5 criado\n");
            return 0;
        }
        wait(NULL); // Filho 2 espera Filho 5
        return 0;
    }

    filho3 = fork();
    if (filho3 == 0) {
        printf("Filho 3 criado\n");
        return 0;
    }

    // Processo Pai
    wait(NULL); // Pai espera todos os filhos
    wait(NULL);
    wait(NULL);

    printf("Processo Pai finalizou\n");
    return 0;
}