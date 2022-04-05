#Transporte-se no tempo e volte para a época de escola! Lembra do dia em que aprendeu
#a encontrar o valor de X nas equações de 2º grau? Aquelas que tinham uma carinha 
#parecida com Ax² + Bx + C = 0?
#Vamos dar um presente ao seu “eu” do passado e criar um programa no qual o usuário
#  só tenha que escrever os valores de A, B e C e nosso programa vai se encarregar
#  de fazer os cálculos.

import math

a = float(input("Informe o valor de A"))
b = float(input("Informe o valor de B"))
c = float(input("Informe o valor de C"))
delta = b * b - 4 * a *c

if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("Para a equação {}x² + {}x + {} = 0, obtivemos os seguintes valores: x1 = {} e x2 = {}".format(a, b, c, x1, x2))
elif delta == 0
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    print("Para a equação {}x² + {}x + {} = 0, obtivemos o seguinte valor: x = {}".format(a, b, c, x))
else:
    print("Para a equação {}x² + {}x + {} = 0, não existem valores reais para x".format(a, b, c))