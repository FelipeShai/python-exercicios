 #– Você deve elaborar um algoritmo implementado em Python em que o usuário informe quantos alimentos consumiu naquele dia e depois possa 
 #informar o número de calorias de cada um dos alimentos. Como não estudamos listas neste capítulo, você não deve se preocupar em armazenar 
 #todas as calorias digitadas, mas deve exibir o total de calorias no final.

quantidade = int(input("Digite a quantidade de alimentos consumidos em um dia:  "))
resultado = 0
for i in range (1, quantidade + 1):
    caloria = int(input("Digite o valor calórico do alimento {}: ".format(i)))
    resultado = caloria + resultado
print("O resultado é: {}".format(resultado))

