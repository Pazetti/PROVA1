lista=[]
for i in range(3):
   num=int(input(f"Insira o numero {i+1}: "))
   lista.append(num)
   lista.sort(reverse=True)

print(lista)