i = 1
lista = []
while(1):
	coisa = int(input('Lista Eterna de Numeros - Coisas ' + str(i) + ': '))
	i += 1
	if(coisa == -1):
		print('Até que fim')
		break
	else:
		lista.append(coisa)

print(lista)
