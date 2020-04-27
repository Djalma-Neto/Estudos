class Pessoa():
	nome = None
	idade = None
	ano = None
	status = None

	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade

	def Ano(self):
		self.ano = 2020 - self.idade

	def Info(self):
		print("Nome: {}, Idade: {}, Ano: {}, Status: {}".format(self.nome, self.idade, self.ano, self.status))

	def Status(self):
		print("Escolha um status(1~3): ")
		print("1- Parar.\n2- Andar.\n3- Correr.")
		stat = input()
		if(stat == "1"):
			if(self.status == "Parado"):
				print("Já está parado!")
			else:
				print("Parou")
				self.status = "Parado"

		elif(stat == "2"):
			if(self.status == "Andando"):
				print("Já está Andando!")
			else:
				print("Andou")
				self.status = "Andando"

		elif(stat == "3"):
			if(self.status == "Correndo"):
				print("Já está Correndo!")
			else:
				print("Correndo")
				self.status = "Correndo"


joao = Pessoa("João", 22)
joao.Ano()

val = True

while val:
	joao.Status()
	joao.Info()
	num = input("Continuar?: (S-N)")
	if(num == "N" or num =="n"):
		val = False
