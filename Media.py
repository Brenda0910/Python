notaA = float(input("Digite a primeira  nota: "))
notaB = float(input("Digite a segunda nota: "))

#Calcular media

mediafinal = (notaA + notaB) /2

#Verificação
if mediafinal >= 7.0:
    print("A média: %.1f - Aprovado" % mediafinal)
else:
    print("A média: %.1f - Reprovado" % mediafinal)

