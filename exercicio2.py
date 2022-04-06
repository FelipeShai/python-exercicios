# A loja virtual FIAP Wear, que vende roupas personalizadas da instituição, 
#disponibilizou no mês do seu aniversário o cupom NIVER10, que concede 10% de 
#desconto no valor total de uma compra feita no site.
#Caso o cliente digite o cupom corretamente, deverá ser informado do valor final 
#da compra já com o desconto aplicado. Caso digite o cupom de maneira incorreta, 
#deverá ser informado do valor da compra sem o desconto.

valor:float = input("Digite o valor da compra: ")
cupom:str = input("Digite o valor do cupom: ")
valorfinal:float
if cupom.upper() == "NIVER10":
    valorfinal = float(valor) * 0.9
    print("O seu cupom de 10% foi aplicado, o valor atual é: {}".format(valorfinal))
else:
    print("CUPOM INVÁLIDO")
    