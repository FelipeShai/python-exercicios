#Muitos professores preferem adotar modelos diferentes de provas quando dão aulas para turmas muito grandes. 
#Por essa razão, a escola de inglês JoWell Sant’ana, em que todas as turmas são compostas por 50 alunos, 
#solicitou que você criasse um sistema capaz de atender ao seguinte requisito: o professor deve digitar primeiro
#as notas dos 25 alunos que têm número ímpar na chamada (1, 3, 5..., 47, 49) e depois as notas dos 25 alunos que
#têm número par (2, 4, 6..., 48, 50). O sistema deve calcular e exibir a média de cada uma das metades da sala e
#informar, ao final, qual delas teve a maior nota.

contador = 0.0
turma1 = 0.0
turma2 = 0.0
media1 = 0.0
media2 = 0.0

print("Começando com os alunos de número ímpar.")
for contador in range(1,50,2):
    nota1 = float(input("Digite a nota do aluno {}:  ".format(contador)))
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES")
    turma1 = turma1 + nota1
media1 = turma1 / 25
print("A média é: {}".format(media1))

print("Agora os alunos de número par.")

for contador in range(2,51,2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES")
    nota2 = float(input("Digite a nota do aluno {}:  ".format(contador)))
    turma2 = turma2 + nota2
media2 = turma2 / 25
print("A média é: {}".format(media2))