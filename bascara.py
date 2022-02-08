a = float(input("Digite aqui o valor de a(este valor deve ser diferente de 0): "))
b = float(input("Digite aqui o valor de b: "))
c = float(input("Digite aqui o valor de c: "))
def lin():
    print(80 * "*");

import math
delta = float((b ** 2) - (4 * a * c))

if a == 0:
    lin()
    print("O valor de a não deve ser menor que zero!")
    lin()
if delta < 0:
    lin()
    print("esta equação não possui raízes reais")
    lin()
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    if x1 < x2:
        lin()
        print("as raízes da equação são",x1,"e",x2)
        lin()
    else:
        lin()
        print("as raízes da equação são",x2,"e",x1)
        lin()
if delta == 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    lin()
    print("a raiz dupla desta equação é",x1)
    lin()




