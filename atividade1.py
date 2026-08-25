#1. Apresentacao: Crie um programa que peca o nome, sobrenome e profissao do usuario. Guarde-os em variaveis separadas (utilize type hints para definir que sao do tipo str) e exiba uma frase formatada. Ex: “Ola, Pedro Silva. Sua profissao e Engenheiro.” 

Nome:str=input("Digite seu nome: ")
sobrenome:str=input("Digite seu sobre nome: ")
profissao:str=input("Digite a sua profissao: ")

print(f"Olá, meu nome é {Nome} {sobrenome} e sou {profissao}")