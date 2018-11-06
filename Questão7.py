vetor = []
print ('Digite 10 numeros')
for i in range(10):
 	vetor.append(input('Numero '+ str(i+1) + ':\n' ))

vetor2 = []
print ('Digite 10 numeros')
for i in range(10):
 	vetor2.append(input('Numero '+ str(i+1) + ':\n' ))

vetor3 = vetor+vetor2
print(vetor3)
