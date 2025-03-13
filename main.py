# Função 1: Fatorial de um Número
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

# Função 2: Soma de uma Lista
def soma_lista(lista):
    if not lista:
        return 0
    else:
        return lista[0] + soma_lista(lista[1:])

# Função 3: Inversão de String
def inverte_string(s):
    if len(s) == 0:
        return s
    else:
        return inverte_string(s[1:]) + s[0]

# Função 4: Poupança – Dólar Americano
def calcular_poupanca(balance, months, total_invested, total_interest, reached_100k, months_100k, invested_100k, interest_100k):
    if balance >= 1e6:
        return (months_100k, invested_100k, interest_100k, months, total_invested, total_interest)
    else:
        new_balance = balance * 1.0005 + 500
        new_months = months + 1
        new_total_invested = total_invested + 500
        new_total_interest = total_interest + (balance * 0.0005)
        
        new_reached_100k = reached_100k
        new_months_100k = months_100k
        new_invested_100k = invested_100k
        new_interest_100k = interest_100k
        
        if not reached_100k and new_balance >= 1e5:
            new_reached_100k = True
            new_months_100k = new_months
            new_invested_100k = new_total_invested
            new_interest_100k = new_total_interest
        
        return calcular_poupanca(new_balance, new_months, new_total_invested, new_total_interest, new_reached_100k, new_months_100k, new_invested_100k, new_interest_100k)

# Função 5: Bitcoin (Exemplo simplificado)
btc_prices_2024 = [30000] * 12  # Valores hipotéticos

def calcular_bitcoin(current_month, months_passed, total_invested, total_btc, btc_prices, reached_100k, reached_1m, reached_1btc, months_100k, months_1m, months_1btc, invested_100k, invested_1m, invested_1btc, reais_100k, reais_1m, btc_1):
    if reached_100k and reached_1m and reached_1btc:
        return (months_100k, invested_100k, reais_100k, months_1m, invested_1m, reais_1m, months_1btc, invested_1btc, btc_1)
    else:
        price = btc_prices[current_month % 12]
        btc_bought = 250 / price
        new_total_btc = total_btc + btc_bought
        new_total_invested = total_invested + 250
        new_months_passed = months_passed + 1
        new_total_reais = new_total_btc * price
        
        # Atualizar marcos
        new_reached_100k, new_reached_1m, new_reached_1btc = reached_100k, reached_1m, reached_1btc
        new_months_100k, new_invested_100k, new_reais_100k = months_100k, invested_100k, reais_100k
        new_months_1m, new_invested_1m, new_reais_1m = months_1m, invested_1m, reais_1m
        new_months_1btc, new_invested_1btc, new_btc_1 = months_1btc, invested_1btc, btc_1
        
        if not reached_100k and new_total_reais >= 1e5:
            new_reached_100k = True
            new_months_100k, new_invested_100k, new_reais_100k = new_months_passed, new_total_invested, new_total_reais
        if not reached_1m and new_total_reais >= 1e6:
            new_reached_1m = True
            new_months_1m, new_invested_1m, new_reais_1m = new_months_passed, new_total_invested, new_total_reais
        if not reached_1btc and new_total_btc >= 1:
            new_reached_1btc = True
            new_months_1btc, new_invested_1btc, new_btc_1 = new_months_passed, new_total_invested, new_total_btc
        
        return calcular_bitcoin((current_month + 1) % 12, new_months_passed, new_total_invested, new_total_btc, btc_prices, new_reached_100k, new_reached_1m, new_reached_1btc, new_months_100k, new_months_1m, new_months_1btc, new_invested_100k, new_invested_1m, new_invested_1btc, new_reais_100k, new_reais_1m, new_btc_1)

# Função 6: Ações (Exemplo simplificado)
acoes_precos = [[10.0] * 12, [20.0] * 12, [30.0] * 12]  # Valores hipotéticos
acoes_dividendos = [[0.01] * 12, [0.02] * 12, [0.03] * 12]  # Dividendos mensais

def calcular_acoes(current_month, months_passed, total_invested, qtd_acoes, dividendos, reached_100k, reached_1m, meses_100k, meses_1m, investido_100k, investido_1m, div_100k, div_1m):
    if reached_100k and reached_1m:
        return (meses_100k, investido_100k, div_100k, meses_1m, investido_1m, div_1m)
    else:
        total_value = sum([qtd_acoes[i] * acoes_precos[i][current_month % 12] for i in range(3)])
        total_dividendos = sum([qtd_acoes[i] * acoes_precos[i][current_month % 12] * acoes_dividendos[i][current_month % 12] for i in range(3)])
        
        # Comprar ações
        investimento = 80
        for i in range(3):
            qtd_acoes[i] += (investimento / 3) / acoes_precos[i][current_month % 12]
        
        new_total_invested = total_invested + investimento
        new_months_passed = months_passed + 1
        new_total_value = sum([qtd_acoes[i] * acoes_precos[i][current_month % 12] for i in range(3)])
        new_dividendos = dividendos + total_dividendos
        
        # Atualizar marcos
        new_reached_100k, new_reached_1m = reached_100k, reached_1m
        new_meses_100k, new_investido_100k, new_div_100k = meses_100k, investido_100k, div_100k
        new_meses_1m, new_investido_1m, new_div_1m = meses_1m, investido_1m, div_1m
        
        if not reached_100k and new_total_value >= 1e5:
            new_reached_100k = True
            new_meses_100k, new_investido_100k, new_div_100k = new_months_passed, new_total_invested, new_dividendos
        if not reached_1m and new_total_value >= 1e6:
            new_reached_1m = True
            new_meses_1m, new_investido_1m, new_div_1m = new_months_passed, new_total_invested, new_dividendos
        
        return calcular_acoes((current_month + 1) % 12, new_months_passed, new_total_invested, qtd_acoes, new_dividendos, new_reached_100k, new_reached_1m, new_meses_100k, new_meses_1m, new_investido_100k, new_investido_1m, new_div_100k, new_div_1m)

# Menu de seleção
def main():
    print("Escolha a função:")
    print("1. Fatorial")
    print("2. Soma de Lista")
    print("3. Inverter String")
    print("4. Poupança (US$)")
    print("5. Bitcoin")
    print("6. Ações")
    opcao = input("Digite o número da função: ")
    
    if opcao == "1":
        n = int(input("Digite um número inteiro positivo: "))
        print(f"Fatorial de {n} é {fatorial(n)}")
    elif opcao == "2":
        lista = list(map(float, input("Digite números separados por espaço: ").split()))
        print(f"Soma da lista: {soma_lista(lista)}")
    elif opcao == "3":
        s = input("Digite uma string: ")
        print(f"String invertida: {inverte_string(s)}")
    elif opcao == "4":
        meses_100k, investido_100k, juros_100k, meses_1m, investido_1m, juros_1m = calcular_poupanca(0, 0, 0, 0, False, 0, 0, 0)
        anos_100k, meses_resto_100k = divmod(meses_100k, 12)
        anos_1m, meses_resto_1m = divmod(meses_1m, 12)
        print(f"Marco 100k: {anos_100k} anos e {meses_resto_100k} meses | Investido: R${investido_100k:.2f} | Juros: R${juros_100k:.2f}")
        print(f"Marco 1M: {anos_1m} anos e {meses_resto_1m} meses | Investido: R${investido_1m:.2f} | Juros: R${juros_1m:.2f}")
    elif opcao == "5":
        meses_100k, investido_100k, reais_100k, meses_1m, investido_1m, reais_1m, meses_1btc, investido_1btc, btc_total = calcular_bitcoin(0, 0, 0, 0, btc_prices_2024, False, False, False, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        anos_100k, meses_resto_100k = divmod(meses_100k, 12)
        anos_1m, meses_resto_1m = divmod(meses_1m, 12)
        anos_1btc, meses_resto_1btc = divmod(meses_1btc, 12)
        print(f"Marco 100k: {anos_100k} anos e {meses_resto_100k} meses | Investido: R${investido_100k:.2f} | Valor: R${reais_100k:.2f}")
        print(f"Marco 1M: {anos_1m} anos e {meses_resto_1m} meses | Investido: R${investido_1m:.2f} | Valor: R${reais_1m:.2f}")
        print(f"Marco 1 BTC: {anos_1btc} anos e {meses_resto_1btc} meses | Investido: R${investido_1btc:.2f} | BTC: {btc_total:.8f}")
    elif opcao == "6":
        meses_100k, investido_100k, div_100k, meses_1m, investido_1m, div_1m = calcular_acoes(0, 0, 0, [0,0,0], 0, False, False, 0, 0, 0, 0, 0, 0)
        anos_100k, meses_resto_100k = divmod(meses_100k, 12)
        anos_1m, meses_resto_1m = divmod(meses_1m, 12)
        print(f"Marco 100k: {anos_100k} anos e {meses_resto_100k} meses | Investido: R${investido_100k:.2f} | Dividendos: R${div_100k:.2f}")
        print(f"Marco 1M: {anos_1m} anos e {meses_resto_1m} meses | Investido: R${investido_1m:.2f} | Dividendos: R${div_1m:.2f}")
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()