notas = []

otimo = 0

bom = 0

regular = 0



for w in range(5):

    notas.append(int(input("Digite a nota: ")))

print(notas)

for a in notas:

    if (a == 3):

        otimo += 1

    elif (a == 2):

        bom += 1

    elif (a == 1):

        regular += 1

print(otimo, " pessoas disseram ser otimo, ",

      bom, " pessoas disseram ser bom e ",

      regular, " pessoas disseram ser regular")