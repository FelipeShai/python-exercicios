#– Observando o mercado de educação infantil, você e sua equipe decidem criar um aplicativo por meio do qual as crianças aprendam a controlar
#os seus gastos. Como forma de validar um protótipo, foi solicitado que você crie um script simples, em que o usuário deve informar QUANTAS 
#TRANSAÇÕES  financeiras realizou ao longo de um dia e, na sequência, deve informar o VALOR DE CADA UMA das transações que realizou. 
#Seu programa deverá exibir, ao final, o valor total gasto pelo usuário, bem como a média do valor de cada transação.

transacao = int(input("Quantas transações você fez: "))
resultado = 0
for i in range (1, transacao + 1):
    valor = float(input("Valor da transação {}: ".format(i)))
    resultado = valor + resultado
media = resultado / transacao
print("O valor total é = {}".format(resultado))
print("A média é = {}".format(media))



      