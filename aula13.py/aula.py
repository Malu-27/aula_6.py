import unittest
from prova import Prova
# from aula13 import Calcular

# class CalcularTest(unittest.TestCase):
#     def test_calcular(self):
#         self.assertEqual(calcular(1,2), 3)
#         self.assertNotEqual
# unittest.main(argv=[''], exit=False)
class ProvaTest(unittest.TestCase):
    def test_adicionaQuestao(self):
        questao = "Testo"
        p = Prova()
        p.adicionar(questao, "")
        self.assertIn("Testo", p.questoes)

unittest.main(argv=[''], exit=False)
