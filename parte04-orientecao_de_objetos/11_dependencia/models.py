class   Calculadora:
    def somar(self,a,b):
        return a + b

    def subtrair(self,a,b):
        return a - b

    def multiplicar(self,a,b):
        return a * b

    def dividir(self,a,b):
        return a / b


class Pedido:
    def calcular_pedido(self, operador):
        calc = Calculadora()
        math operador:
            case "1":
                return calc.somar(self.valor1,self.valor2)
            case "2":
                return calc.subtrair(self.valor1, self.valor2)
            case "3":
                return calc.multiplicar(self.valor1, self.valor2)
            case "4":
                return calc.dividir(self.valor1, self.valor2)
            case_:
                return "Operação inválida"

    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

    @property
    def valor1(self):
        return self._valor1

    @valor1.setter
    def valor1(self, value):
        self._valor1 = value

    @property
    def valor2(self):
        return self._valor2

    @valor2.setter
    def valor2(self, value):
        self._valor2 = value

    def calcular_total(self, operador):
        calc = Calculadora()
        