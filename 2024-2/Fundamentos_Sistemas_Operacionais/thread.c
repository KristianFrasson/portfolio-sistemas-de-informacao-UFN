/*
   Exemplo de criação de threads com POSIX threads.
   Este exemplo cria duas threads que executarão concorrentemente a função mostraCidade
*/
#include <pthread.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


//Na biblioteca pthread, sempre a função que será executada pelas threads deve retornar void* e sempre tem um argumento void*,
//ou seja, ponteiro para void (ponteiro genérico). Se precisarmos passar mais de um dado para a thread, devemos usar os tipos
// compostos em C, como por exemplo, struct.
void* mostraCidade(void* nome)
{
       int aux1, aux2, aux3, count;

       if (strcmp(nome, "Santa Maria") == 0)
             count = 50;
       else
             count = 100;

       for(aux1=0; aux1<count; aux1++)
       {
             printf("%d %s\n", aux1, (char *) nome);
             /* Cria uma espera, sem suspender a thread */
             for(aux2=rand()/10000;aux2>0;aux2--)
               for(aux3=10;aux3>0;aux3--);
       }
       pthread_exit(0);
}


// a função principal main(), equivale à execução da thread principal do programa.
int main()
{
       int i;
       pthread_t thUm, thDois; //observe que é necessário declarar uma variável do tipo thread pthread_t, para cada thread a ser criada.


       pthread_create(&thUm, 0, mostraCidade, "Santa Maria");
       pthread_create(&thDois, 0, mostraCidade, "Porto Alegre");

       //A thread principal espera as threads criadas. O primeiro argumento de pthread_join é a variável que identifica a thread
       // e o segundo, como o retorno é nulo, é zero, pois não precisa armazenar o retorno da thread
       pthread_join(thUm, 0);
       pthread_join(thDois, 0);

       printf("Fim do Thread Principal\n");
       return 0;
}
