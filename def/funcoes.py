def calcular_imc(peso, altura):
    indice = peso / (altura **2)
    return indice
oloko = calcular_imc(75, 1.75)
print(f"{oloko:.2f}")    