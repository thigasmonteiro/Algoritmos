distancia = float(input("Qual a distancia a ser percorrida em Km? :"))
velocidade = int(input ( "Qual a velociade do veículo em Km/h? :"))

tempo = ((distancia) / (velocidade))
minuto = ((tempo) * (60))

print ("O tempo percorrido em horas é de:", tempo)
print ("O tempo percorrido em minutos é de:", minuto)