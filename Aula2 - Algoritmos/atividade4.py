salario  = float(input("Informe seu salario; "))
porcentagem = float(input("Informe a porcentagem de aumento :"))

aumento = ((salario * porcentagem) / 100 )
valorfinal = (salario + aumento)

print(valorfinal)