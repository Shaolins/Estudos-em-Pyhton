nome              = input ("digite seu nome: ")
idade             = int(input("digite a sua idade:"))
nota1             = float(input("digite sua nota de português:"))
nota2             = float(input("digite sua nota de matematica:"))
nota_trabalho     = float(input("digite a nota do trabalho: "))
frequencia        = int(input("digite a sua frequência de 0 a 100:"))
entrega_trabalhos = input("entregou todos os trabalhos (sim/não):").strip().capitalize()

media = (nota1 + nota2) /2


if idade >5:
    
    if frequencia >= 75:
        
        if nota1 >=0 and nota2>=0 and nota_trabalho >= 0:
            
            if entrega_trabalhos == "Sim":
                
                if media >=5:
                    
                    if nota_trabalho >= 6 or media >=8:
    
                        print("Parabéns você passou de ano")
                    else:
                     
                        print("não teve nota o suficiente")
                else:
                     
                    print("sua média foi baixa")
            else:
                print("faça uma recuperação")    
        else:
            
             print("não possuí nota")    
    else:
     
        print("não possui frequência o suficiente ")
else:

    print("infelizmente vc não tem idade o suficiente")