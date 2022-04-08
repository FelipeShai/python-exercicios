#Os alunos da sua turma fizeram uma votação para escolher qual dia da semana é o melhor para a realização das lives. 
#Desenvolva um programa em que o usuário informe a quantidade de votos que cada um dos 5 dias da semana (segunda-feira,
#terça-feira, quarta-feira, quinta-feira e sexta-feira) obtiveram, verifique e exiba qual dia foi o escolhido.  

segunda = float(input("Por favor, digite o número total de votos na segunda-feira:  "))
terca = float(input("Por favor, digite o número total de votos na terça-feira:  "))
quarta = float(input("Por favor, digite o número total de votos na quarta-feira:  "))
quinta = float(input("Por favor, digite o número total de votos na quinta-feira:  "))
sexta = float(input("Por favor, digite o número total de votos na sexta-feira:  "))

if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print("Segunda foi o dia escolhido pela turma")

elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print("Terça foi o dia escolhido pela turma")

elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    print("Quarta foi o dia escolhido pela turma")

elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
    print("Quinta foi o dia escolhido pela turma")

elif sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta:
    print("Sexta foi o dia escolhido pela turma")
