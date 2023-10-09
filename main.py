# Função para calcular o valor com base na porcentagem
def calcular_valor_porcentagem(renda_total, porcentagem):
    return (porcentagem / 100) * renda_total

# Função para calcular a porcentagem ideal de gastos essenciais com base no valor total
def calcular_porcentagem_gastos_essenciais_ideal(renda_total):
    return 40.0

# Entrada da renda total
renda_total = float(input("Informe o valor total: "))

# Entrada dos gastos essenciais do mês
gastos_essenciais = float(input("Informe o valor dos gastos essenciais: "))

# Cálculo da porcentagem ideal de gastos essenciais
porcentagem_gastos_essenciais_ideal = calcular_porcentagem_gastos_essenciais_ideal(renda_total)

# Cálculo do valor ideal de gastos essenciais com base na porcentagem
valor_gastos_essenciais_ideal = calcular_valor_porcentagem(renda_total, porcentagem_gastos_essenciais_ideal)

# Cálculo do valor restante após subtrair os gastos essenciais
valor_restante = renda_total - gastos_essenciais

# Cálculo das porcentagens para "Estilo de Vida", "Dívidas" e "Investimentos"
porcentagem_estilo_de_vida = 50
porcentagem_dividas = 35
porcentagem_investimentos = 15

# Cálculo dos valores para "Estilo de Vida", "Dívidas" e "Investimentos" com base nas porcentagens
valor_estilo_de_vida = calcular_valor_porcentagem(valor_restante, porcentagem_estilo_de_vida)
valor_dividas = calcular_valor_porcentagem(valor_restante, porcentagem_dividas)
valor_investimentos = calcular_valor_porcentagem(valor_restante, porcentagem_investimentos)

# Nomes e porcentagens dos itens de "Estilo de Vida"
itens_estilo_de_vida = {
    "Entretenimento": 10,
    "Refeições fora de casa": 30,
    "Viagens e Férias": 10,
    "Hobbies": 10,
    "Roupas": 30,
    "Educação": 10
}

negrito = "\033[1m"

# Cálculo dos valores para cada item de "Estilo de Vida" com base nas porcentagens
valores_itens_estilo_de_vida = {item: calcular_valor_porcentagem(valor_estilo_de_vida, porcentagem) for item, porcentagem in itens_estilo_de_vida.items()}

# Exibição dos resultados
print(f"{negrito}Valor total: {renda_total:.2f}")
print(f"{negrito}Valor do gastos essenciais ideal (40% do valor total): {valor_gastos_essenciais_ideal:.2f}")
print(f"{negrito}Valor em porcentagem do valor de gastos essenciais informado: {(gastos_essenciais / renda_total) * 100:.2f}%")

print("{negrito}Itens de Estilo de Vida:")
print()

for item, valor in valores_itens_estilo_de_vida.items():
    print(f"{negrito}{item}: R${valor:.2f}")

print()
print(f"{negrito}Valor das Estilo de vida: R${valor_estilo_de_vida:.2f}")
print(f"{negrito}Valor das dívidas: R${valor_dividas:.2f}")
print(f"{negrito}Valor para investimento: R${valor_investimentos:.2f}")
