# Tipo de dado novo: Fração
# valor numérico para numerador e denominador

import math

class Fracao:
  def __init__(self, num, den):
    self.num = num
    self.den = den if den != 0 else 1  # evita divisão por zero

  def __str__(self):
    return f"{self.num}/{self.den}"
  
  # soma
  def __add__(self, rhs):
    if self.den == rhs.den:
      return Fracao(self.num + rhs.num, self.den)
    else:
      mmc = math.lcm(self.den, rhs.den)
      return Fracao(self.num * (mmc // self.den) + rhs.num * (mmc // rhs.den), mmc)
  
  # comparador ==, !=
  def __eq__(self, rhs): # right hand side
    if (self.den == rhs.den):
      return self.num == rhs.num
    else:
      return self.num * rhs.den == rhs.num * self.den
  
  # comparador >, <
  def __gt__(self, rhs):
    if (self.den == rhs.den):
      return self.num > rhs.num
    else:
      return self.num * rhs.den > rhs.num * self.den
  
  # comparador >=, <=
  def __ge__(self, rhs):
    if (self.den == rhs.den):
      return self.num >= rhs.num
    else:
      return self.num * rhs.den >= rhs.num * self.den

if __name__ == '__main__':
  fracao1 = Fracao(1, 3)
  print(fracao1)

  fracao2 = Fracao(2, 6)
  print(fracao2)

  print(fracao1 > fracao2)