estoques = [50, 3, 120, 7, 0, 45, 2]
somar = 0 
produtos = 0
baixo = 0


for estoque in estoques:
    somar = somar + estoque 
    if estoque <1:
        produtos = produtos + 1
    elif estoque <10:
        baixo = baixo + 1


print(f"o total no estoque é: {somar}")
print(f" os produtos que estão em falta são {produtos}")
print("a quantidade de produtos com baixo estoque é: ",baixo)












    

