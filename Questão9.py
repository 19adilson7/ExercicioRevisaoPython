N_veiculo = []
kms = []
km = 0
for c in range(5):
    print(f"\nVeiculo {c + 1}")
    N_veiculo.append(input("Nome do veiculo: "))
    km = float(input("Kilometros por litro: "))
    kms.append(km)

print("\nFinal")
mnr = 0
n_om_e = ' '
for c,d in enumerate(N_veiculo):
    print(f"{c + 1}\t -\t{d}\t - \t{kms[c]} -\t{1000 / kms[c]:.2f}\t -\t{1000 / kms[c] * 2.25:.2f}")
    if kms[c] > mnr:
        mnr = kms[c]
        n_om_e = N_veiculo[c]

print(f"\nO menor consumo e do {n_om_e}\n")
