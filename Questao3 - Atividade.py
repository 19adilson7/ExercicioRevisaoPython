pergunta1 = str(input("Telefonou para a vítima? "))
pergunta1 = pergunta1.upper()
pergunta2 = str(input("Esteve no local do crime? "))
pergunta2 = pergunta2.upper()
pergunta3 = str(input("Mora perto da vítima? "))
pergunta3 = pergunta3.upper()
pergunta4 = str(input("Devia para a vítima? "))
pergunta4 = pergunta4.upper()
pergunta5 = str(input("Já trabalhou com a vítima? "))
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
