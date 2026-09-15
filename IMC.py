nome = input("qual é o seu nome? ")
altura = float(input("qual é a sua altura? "))
peso = float(input("qual é o seu peso? "))

IMC = peso /(altura ** 2)

if IMC < 18.5:
    print("você está abaixo do peso ideal.")

elif IMC >= 18.5 and IMC < 25:
    print("você está com o peso ideal.")

elif IMC >= 25 and IMC < 29.9:
    print("você está com sobrepeso.")

else:
    print("você está com obesidade.")

print(f"Olá, {nome}! Seu IMC é {IMC:.2f}")
