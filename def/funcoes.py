def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

peso = 75
altura = 1.75

imc = calcular_imc(peso, altura)
categoria = classificar_imc(imc)

print(f"IMC: {imc:.2f} - Categoria: {categoria}")
