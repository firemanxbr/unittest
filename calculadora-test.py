import unittest 
from should_dsl import * 
from calculadora import Calculadora
 
class CalculadoraTest(unittest.TestCase):
    def testa_soma(self):
        Calculadora.soma(1,1) |should| equal_to(2)
 
if __name__ == '__main__':
    unittest.main()
