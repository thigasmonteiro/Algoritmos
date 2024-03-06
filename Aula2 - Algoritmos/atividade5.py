valormerc = float(input("Insira o valor da mercadoria; "))
porcentual = float(input("Insira o valor de desconto:"))

desconto = ((valormerc * porcentual) / 100)

valorfinal = ((valormerc) - (desconto) )

print ("O valor decontado foi de: ", desconto)
print( "O valor final com a se pagar é de : ", valorfinal)