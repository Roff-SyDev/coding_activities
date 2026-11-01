# Contador de respostas desejadas.
qtd_excelente = 0
qtd_ruim = 0

# Definindo a quantidade de entrevistados.
total_entrevistados = 50

print("=== PESQUISA DE ATENDIMENTO AO CLIENTE ===")

# Loop para coleta de dados.
for i in range(1, total_entrevistados + 1):
    print(f"\n--- Entrevistado {i} de {total_entrevistados} ---")
    
    # Coletando dados.
    nome = input("Digite o nome do entrevistado: ")
    idade = int(input("Digite a idade do entrevistado: "))
    
    print("Avalie o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    
    opiniao = int(input("Digite o número da sua opinião (1, 2 ou 3): "))
    
    # Estrutura de decisão que verifica a opinião.
    if opiniao == 1:
        qtd_excelente += 1
    elif opiniao == 3:
        qtd_ruim += 1
    elif opiniao == 2:
        # Opção "Bom".  
        pass
    else:
        print("Opção inválida! Resposta não contabilizada para as estatísticas.")

# Exibição dos resultados finais.
print("\n" + "="*45)
print("       RESULTADO FINAL DA PESQUISA")
print("="*45)
print(f"a) Quantidade de respostas 'EXCELENTE': {qtd_excelente}")
print(f"b) Quantidade de respostas 'RUIM': {qtd_ruim}")
print("="*45)
