def triangulo_valido(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a > (b + c):
        return False
    if b > (a + c):
        return False
    if c > (a + b):
        return False
    return True

def calcula_lados(x0,y0,x1,y1):
    d1 = (x1 - x0)**2
    print(d1)
    d2 = (y1 - y0)**2
    print(d2)
    d = (d1 + d2) ** (1/2)
    print(d)
    return d

def perimetro(a, b, c):
    return (a + b + c)

def area(a, b, c):
    #usando fórmula de Heron
    p = perimetro(a,b,c)/2
    area = p * (p-a) * (p-b) * (p-c)
    return area**(1/2)