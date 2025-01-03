# Tipo de dado novo: Moeda
# valor numérico
# qual o país / nome / sigla (código)

from utils import CURRENCY_NAMES, get_exchange_rate

class Currency:
  def __init__(self, value, code):
    self.value = value
    self.code = code.upper()

  def __str__(self):
    return f"{self.value:.2f} {self.code}"
  
  # comparador ==, !=
  def __eq__(self, rhs): # right hand side
    if (self.code == rhs.code) and (self.value == rhs.value):
      return self.value == rhs.value
    return self == rhs.convert(self.code)
  
  # comparador >, <
  def __gt__(self, rhs):
    if self.code == rhs.code:
      return self.value > rhs.value
    return self > rhs.convert(self.code)
  
  # comparador >=, <=
  def __ge__(self, rhs):
    return (self > rhs) or (self == rhs)
  
  # soma
  def __add__(self, rhs):
    if self.code == rhs.code:
      return Currency(self.value + rhs.value, self.code)
    raise ValueError("Moedas devem ser do mesmo país!")

  # negação
  def __neg__(self):
    return Currency(-self.value, self.code)
  
  # subtração
  def __sub__(self, rhs):
    return self + (-rhs)
  
  # multiplicação
  def __mul__(self, rhs):
    if isinstance(rhs, int) or isinstance(rhs, float):
      return Currency(self.value * rhs, self.code)
    raise ValueError(f"{rhs} deve ser um NÚMERO!")
  
  # multiplicação - função para os casos onde a chamada é "N * MOEDA"
  def __rmul__(self, lhs):
    return self * lhs
  
  # divisão
  def __truediv__(self, rhs):
    if isinstance(rhs, int) or isinstance(rhs, float):
      return Currency(self.value / rhs, self.code)
    raise ValueError(f"{rhs} deve ser um NÚMERO!")
  
  # divisão
  def __floordiv__(self, rhs):
    if isinstance(rhs, int) or isinstance(rhs, float):
      return Currency(self.value // rhs, self.code)
    raise ValueError(f"{rhs} deve ser um NÚMERO!")
  
  def convert(self, to_code):
    to_code = to_code.upper()
    rate = get_exchange_rate(self.code, to_code)
    return Currency(rate * self.value, to_code)

if __name__ == '__main__':
  moeda1 = Currency(100, "Usd")
  print(moeda1)
  print(moeda1.convert("BRL"))