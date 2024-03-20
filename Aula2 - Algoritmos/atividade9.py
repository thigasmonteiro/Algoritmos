cigarrosDia = int(input("Insira a quantidade de cigarros que você fuma por dia:"))
anosFumado = int(input("Insira a quantidade de anos que voce fuma :"))

reducao_em_minutos = (anosFumado * 365 * cigarrosDia * 10)
reducao_em_dias = ((reducao_em_minutos1) / (24*60))
print(f"Você perdeu", reducao_em_dias, "de vida")