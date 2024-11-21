def calcular_tempo_atendimento():
    # Solicitar o número de clientes
    n_clientes = int(input("Digite o número de clientes na fila: "))
    
    # Solicitar o tempo que o processador leva para processar cada um dos processos
    tempo_processador = int(input("Digite o tempo que o processador leva para processar cada processo: "))
    
    # Lista para armazenar o tempo de espera de cada cliente
    tempos_espera = []
    
    # Tempo total para o atendimento de todos os processos
    tempo_total = 0
    
    # Loop para cada cliente
    for i in range(n_clientes):
        # Solicitar o número de processos do cliente
        n_processos = int(input(f"Digite o número de processos para o cliente {i + 1}: "))
        
        # O tempo de espera do cliente é igual ao tempo total acumulado até aquele ponto
        tempos_espera.append(tempo_total)
        
        # Calcular o tempo total de processamento para o cliente
        tempo_cliente = n_processos * tempo_processador
        
        # Atualizar o tempo total para o próximo cliente
        tempo_total += tempo_cliente
    
    # Exibir os resultados
    print("\nTempo de espera de cada cliente:")
    for i, tempo in enumerate(tempos_espera):
        print(f"Cliente {i + 1}: {tempo} unidades de tempo")
    
    print(f"\nTempo total para atendimento de todos os processos: {tempo_total} unidades de tempo")

# Chamar a função
calcular_tempo_atendimento()
