nota1 = int(input("Digite a primeira nota : "))
nota2 = int(input("Digite a segunda nota : "))
nota3 = int(input("Digite a terceira nota : "))

Media = (nota1+nota2+nota3)/3

if Media == 10:
  print("Aprovado com Distinção")

elif Media >= 7:
  print("Aprovado")

else:
  print("Reprovado")
