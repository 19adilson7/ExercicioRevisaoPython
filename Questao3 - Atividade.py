pergunta1 = str(input("Telefonou para a v�tima? "))
pergunta1 = pergunta1.upper()
pergunta2 = str(input("Esteve no local do crime? "))
pergunta2 = pergunta2.upper()
pergunta3 = str(input("Mora perto da v�tima? "))
pergunta3 = pergunta3.upper()
pergunta4 = str(input("Devia para a v�tima? "))
pergunta4 = pergunta4.upper()
pergunta5 = str(input("J� trabalhou com a v�tima? "))
pergunta5 = pergunta5.upper()

respostas = [pergunta1, pergunta2, pergunta3, pergunta4, pergunta5]
contadora = 0
for resposta in respostas:
  if resposta == "SIM":
    contadora+=1

if contadora == 2:
  print("Suspeito")

elif contadora>=3 and contadora <=4:
  print("Cumplice")

elif contadora == 5:
  print("Assasino")

else:
  print("Inocente")
