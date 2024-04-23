pop1 = (80000)
pop2 = (200000)
cresc1 = (3/100)
cresc2 = (1.5/100)

for i in range(200):
    novapop1=pop1
    pop1=novapop1*(1+cresc1)

    novapop2=pop2
    pop2=novapop2*(1+cresc2)

    if pop1>=pop2:
        print(f"A cidade 1 ultrapassou a população da cidade 2 no ano {i+1}:")
        break
else:
    print("A população da cidade 1 ainda não ultrapassou a população da cidade 2")