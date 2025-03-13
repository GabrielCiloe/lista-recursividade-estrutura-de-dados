def calcular_poupanca(balance, months, total_invested, total_interest, reached_100k, months_100k, invested_100k, interest_100k):
    if balance >= 1e6:
        return(months_100k, invested_100k, interest_100k, months, total_invested, total_interest)
    else:
        new_balance = balance * 1.0005 + 500
        new_months = months + 1
        new_total_invested = total_invested + 500
        new_total_interest = total_interest + (balance * 0.0005)
        
        new_reached_100k = reached_100k
        new_months_100k = months_100k
        new_invested_100k = invested_100k
        new_interest_100k = interest_100k
        
        if not reached_100k and new_balance > 1e5:
            new_reached_100k = True
            new_months_100k = new_months
            new_invested_100k = new_total_invested
            new_interest_100k = new_total_interest
            
        return calcular_poupanca(new_balance, new_months, new_total_invested, new_total_interest, new_reached_100k, new_months_100k, new_months_100k, new_invested_100k, new_interest_100k)