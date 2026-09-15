num1 = float(input("qual a distância em metros"))

km = num1/1000
hm = num1/100
dam = num1 /10

dm = num1 *10
cm = num1 *100
mm = num1 *1000 
print(f"A distância de {num1}m corresponde a:")
print(f"KM: {km}".ljust(40) + f"DM: {dm}" )
print(f"HM: {hm}".ljust(40) + f"CM: {cm}" )
print(f"DAM: {dam}".ljust(40) + f"MM: {mm}" )




