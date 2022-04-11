#Você foi procurado por um aluno do curso de Produção Multimídia do FIAP ON para 
#desenvolver um trabalho em parceria: um serviço em que as pessoas possam usar um 
#estúdio profissional para gravar seus vídeos para o YouTube com máxima qualidade. 
#O serviço ganha dinheiro por meio de um sistema de assinaturas e de um bônus 
#calculado por uma porcentagem sobre o faturamento que o canal do cliente obteve 
#ao longo do ano.

#Sua tarefa é criar um algoritmo que receba o tipo de assinatura do cliente, o 
#faturamento anual dele e que calcule e exiba qual o valor do bônus que o cliente 
#deve pagar a vocês. A tabela abaixo mostra a porcentagem de acordo com cada nível 
#de assinatura:

tipoassinatura = str(input("Digite, por favor, em mínusculo o tipo da sua assinatura: "))
#if tipoassinatura.lower() != "basic" and tipoassinatura.lower() != "silver" and tipoassinatura.lower() != "gold" and tipoassinatura.lower() != "platinum":
#    print("Plano de assinatura inválido, lembre-se que nossos planos são o basic, silver, gold ou platinum.")
    
faturamentoanual = float(input("Digite o valor do seu faturamento anual: "))
if tipoassinatura.lower() == "basic":
    bonus = faturamentoanual * 0.3
    print("O bônus em um faturamente anual de {} no plano {} é de: {}".format(faturamentoanual,tipoassinatura,bonus))
elif tipoassinatura.lower() == "silver":
    bonus = faturamentoanual * 0.2
    print("O bônus em um faturamente anual de {} no plano {} é de: {}".format(faturamentoanual,tipoassinatura,bonus))
elif tipoassinatura.lower() == "gold":
    bonus = faturamentoanual * 0.1
    print("O bônus em um faturamente anual de {} no plano {} é de: {}".format(faturamentoanual,tipoassinatura,bonus))
elif tipoassinatura.lower() == "platinum":
    bonus = faturamentoanual * 0.05
    print("O bônus em um faturamente anual de {} no plano {} é de: {}".format(faturamentoanual,tipoassinatura,bonus))
else:
    print("Algo não foi digitado corretamente, por favor, tente novamente.")