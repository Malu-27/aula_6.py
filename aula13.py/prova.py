class Prova():
    questoes: list 
    respostas: list
    def __init__(self):
        
        self.questoes = []
        self.respostas = []

    def mostrar_Questoes(self):
        print(self.questoes)
    def mostrar_Respostas(self):
        print(self.questoes)
    def adicionar(self, questao, resposta):
        self.questoes.append(questao)    
        self.respostas.append(resposta)