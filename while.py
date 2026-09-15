soma = 0
i = int(input("digite um numero: "))
while i != 0:
    soma += i        # acumula o número na soma
    i = int(input("digite um numero: "))  # pede o próximo
print(f"soma total: {soma}")