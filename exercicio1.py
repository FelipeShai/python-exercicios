#O doutor Henry Jones Junior estabeleceu uma regra com seus alunos da disciplina de 
#Arqueologia: todos os que obtiverem nota maior do que 8,5 na sua prova semestral 
#serão convidados para uma visita de campo na América do Sul.
#Nosso programa deve solicitar o e-mail e a nota do aluno, exibindo a mensagem 
#“ENVIANDO CONVITE” caso a nota do aluno satisfaça a condição proposta.


email:str = input("Digite seu email: ")
nota:float = input("Digite sua nota: ")
nota = float(nota)
if nota > 8.5:
    print("PARABÉNS! ENVIANDO CONVITE")
else:
    print("Infelizmente, você não foi aprovado para a visita de campo.")