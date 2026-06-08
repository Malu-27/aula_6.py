from abc import ABC, abstractmethod
class Pessoa(ABC):
    nome = str
    idade = int
    __Cpf = str
    
    def __init__(self, nome, idade, Cpf):
        self.nome = nome
        self.idade = idade
        self.__Cpf = Cpf

    def getCpf(self):
        return self.__Cpf
    
    @abstractmethod
    def calcularGanhos(self) -> int:
        pass

class Trabalhador(Pessoa):
    profissao = str
    salario = int
    
    def __init__(self, nome, idade, Cpf, profissao, salario):
        super().__init__(nome, idade, Cpf)
        self.profissao = profissao
        self.salario = salario

    def calcularGanhos(self):
        return self.salario
class PrestadorServico(Pessoa):
    horas_trabalhadas: int
    salario_por_hora: int
    def __init__(self, nome, idade, Cpf, horas_trabalhadas, salario_por_hora):
        super().__init__(nome, idade, Cpf)
        self.horas_trabalhadas = horas_trabalhadas
        self.salario_por_hora = salario_por_hora

    def calcularGanhos(self):
        return self.salario_por_hora * self.horas_trabalhadas
var = Trabalhador("malu", 15, "123.456.789-10", "mentora", 300 )
prestador = PrestadorServico("Joanes", 20, "234.234.234-05", 30, 5)
print(var.calcularGanhos())
print(prestador.calcularGanhos())


        

