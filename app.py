## Entrando com os dados 
equipamento = str(input("Digite o nome do equipamento: "))
potencia = int(input("Indique a potencia em watts:  "))
tempo = float(input("Qual o uso diário em horas:   "))

## Calculando 
consumo_mensal = (potencia*tempo*30) / 1000 

## Exibindo o resultado
print ("Perfeito, o consumo do equipamento informado é:")
print (equipamento)
print (f"Consumo mensal: {consumo_mensal:.3f} kW/mês")
    