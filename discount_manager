# Importando "bibliotecas".

import time

# Digitando o valor total.

time.sleep(2)
print("Olá! Vamos finalizar a sua compra.")
time.sleep(1.5)
total_value = float(input("Digite o valor total da sua compra: "))
time.sleep(1.5)

# Calculando descontos.
if total_value < 200:
    # Desconto baixo, 5%.
    low_disc = 0.05
    discount = total_value * low_disc
    new_value = total_value - discount # "Novo valor" após a aplicação do desconto.
    print(f"Você recebeu um desconto de 5%!")
    time.sleep(0.95) # Tempo de processamento.
    print(f"O desconto em R$ da sua compra é: {new_value} R$.")

# Condicional alternativa.
elif total_value >= 200 and total_value < 300:
    # Desconto médio, 10%.  
    mid_disc = 0.1
    discount = total_value * mid_disc
    new_value = total_value - discount # "Novo valor" após a aplicação do desconto.
    print(f"Você recebeu um desconto de 10%!")
    time.sleep(0.95) # Tempo de processamento.
    print(f"O desconto em R$ da sua compra é de: {new_value} R$.")

# Condicional alternativa.
elif total_value >= 300:
    # Desconto médio, 15%.
    high_disc = 0.15
    discount = total_value * high_disc
    new_value = total_value - discount # "Novo valor" após a aplicação do desconto.
    print(f"Você recebeu um desconto de 15%!")
    time.sleep(0.95) # Tempo de processamento.
    print(f"O desconto em R$ da sua compra é de: {new_value} R$.")
