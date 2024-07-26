import matplotlib.pyplot as plt
import numpy as np
import math

class Polinomio:
    def __init__(self, *tupla):
        if tupla == (0,) or tupla == (0) or tupla == ():
            self.__coeficientes = ()
            self.__grado = 0
        elif type(tupla[0]) == type((1,1)):
            self.__coeficientes = tupla[0]
            self.__grado = len(tupla[0]) - 1
        else:
            self.__coeficientes = tupla
            self.__grado = len(tupla)-1

    def __eq__(self, value: object) -> bool:
        return self.__coeficientes == value.__coeficientes

    def sacar_ceros(self):
        coef = []
        a = False
        for i in self.__coeficientes:
            if i != 0:
                coef.append(i)
                a = True
            elif a:
                coef.append(i)

        self.__coeficientes = tuple(coef)

    def __add__(self, poli2):
        if self.__coeficientes == (0) or self.__coeficientes == () or self.__coeficientes == (0,):
            return poli2.copy()
        elif poli2.__coeficientes == (0) or self.__coeficientes == () or self.__coeficientes == (0,):
            return self.copy()

        coef = []
        if self.__grado > poli2.__grado:
            sum1 = self.copy()
            sum2 = poli2.copy()
        else:
            sum1 = poli2.copy()
            sum2 = self.copy()
        for i in range(sum1.grado() + 1):
            if i < sum1.grado() - sum2.grado():
                coef.append(sum1.__coeficientes[i])
            else:
                coef.append(sum1.__coeficientes[i] + sum2.__coeficientes[i+sum2.__grado-sum1.grado()])

        res = Polinomio()
        res.__coeficientes = tuple(coef)
        res.sacar_ceros()
        res.__grado = len(res.__coeficientes)-1
        return res

    def __sub__(self, poli2):
        sum1 = self.copy()
        sum2 = poli2.copy()
        coef = list(sum2.__coeficientes)
        coef = [-i for i in coef]
        sum2.__coeficientes = tuple(coef)
        return sum1 + sum2

    def __mul__(self, poli2):
        if self.__coeficientes == (0) or self.__coeficientes == () or self.__coeficientes == (0,) or poli2.__coeficientes == (0) or poli2.__coeficientes == () or poli2.__coeficientes == (0,):
            return Polinomio(0)
        mul1 = self.copy()
        mul2 = poli2.copy()
        g = mul1.__grado + mul2.__grado
        coef = [0]*(g+1)

        for i in range(mul1.__grado+1):
            for j in range(mul2.__grado+1):
                coef[g-(mul1.__grado-i)-(mul2.__grado-j)] += mul1.__coeficientes[i]*mul2.__coeficientes[j]

        res = Polinomio()
        res.__coeficientes = tuple(coef)
        res.sacar_ceros()
        res.__grado = len(res.__coeficientes)-1
        return res

    def __truediv__(self, poli2):
        if self.__coeficientes == (0) or self.__coeficientes == () or self.__coeficientes == (0,):
            return Polinomio(0)
        elif poli2.__coeficientes == (0) or poli2.__coeficientes == (0,) or poli2.__coeficientes == ():
            raise ZeroDivisionError("Division por 0")
            return None
        div1 = self.copy()
        div2 = poli2.copy()
        res = Polinomio()
        if div1.grado() >= div2.grado():
            g = div1.grado() - div2.grado()
        else:
            g = div1.grado()

        i = 0
        coef = [0]*(g+1)

        while div1.grado() >= div2.grado():
            coef[i] = div1.__coeficientes[0] / div2.__coeficientes[0]
            coef_aux = [coef[i]] + [0]*(abs(div1.grado() - div2.grado()))

            poli = Polinomio()
            poli.__coeficientes = tuple(coef_aux)
            poli.__grado = len(coef_aux)-1

            div1 = div1 - poli*div2

            i += 1

        res.__coeficientes = tuple(coef)
        res.sacar_ceros()
        res.__grado = len(res.__coeficientes)-1

        return res

    def __pow__(self, x: int):
        f = Polinomio(1)

        for i in range(x):
            f = self * f

        return f

    def __mod__(self, poli2):
        return self - poli2*(self / poli2)

    def grado(self):
        g = len(self.__coeficientes)-1

        for i in self.__coeficientes:
            if i == 0:
                g -=1

            else:
                break

        return g

    def eval(self, x):
        y = 0
        for i in range(len(self.__coeficientes)):
            y += self.__coeficientes[len(self.__coeficientes) - i - 1] * (x ** i)

        return y

    def raices(self):
        if self.grado() > 2 or self.grado() == 0:
            raise TypeError("Operacion no soportada para polinomios con grado > 2 o grado 0.")

        if self.grado() == 1:
            a, b = tuple([i for i in self.__coeficientes])
            return (-b) / a

        a, b, c = tuple([i for i in self.__coeficientes])

        try:
            D = math.sqrt(b ** 2 - 4*a*c)
        except:
            return None

        if D == 0:
            return -b / (2*a)
        else:
            return ((-b + D) / (2*a), (-b - D) / (2*a))

    def graph(self, inicio=-1, final=1, res=50):
        x = np.linspace(inicio, final, res)
        y = self.eval(x)

        fig, ax = plt.subplots()

        ax.plot(x, y)

        plt.show()

    def copy(self):
       res = Polinomio()
       res.__coeficientes = self.__coeficientes
       res.__grado = self.__grado
       return res

    def __repr__(self):
        if self.__coeficientes == (0) or self.__coeficientes == (0,) or self.__coeficientes == ():
            return "0"

        out = []
        for i in range(len(self.__coeficientes)):
            if self.__coeficientes[i] == 0:
                coef = ""
                exp = ""
            elif i == len(self.__coeficientes) - 1:
                 coef = str(self.__coeficientes[i])
                 exp = ""
                 out.append(coef)
            elif i == len(self.__coeficientes) -2:
                if self.__coeficientes[i] == 1:
                    coef = ""
                elif self.__coeficientes[i] == -1:
                    coef = "-"
                else:
                    coef = str(self.__coeficientes[i])
                exp = "X"
                out.append(coef + exp)
            else:
                if self.__coeficientes[i] == 1:
                    coef = ""
                elif self.__coeficientes[i] == -1:
                    coef = "-"
                else:
                    coef = str(self.__coeficientes[i])
                exp = f"X^{self.__grado - i}"
                out.append(coef + exp)


        out_str = out[0]
        for i in range(1,len(out)):
            out_str += " "
            if out[i][0] == "-":
                out_str += "- " + out[i][1::]
            else:
                out_str += "+ " + out[i]

        return out_str

def mcd(poli1: Polinomio, poli2: Polinomio):
    f = poli1.copy()
    g = poli2.copy()

    while not g == Polinomio(0):
        f, g = g, f % g

    return f

def __parsear_str(cadena):
    c = []
    t = ""
    for i in cadena:
        if i != " " and i != "+" and i != "-":
            t += i
        elif i != " ":
            c.append(t)
            c.append(i)
            t = ""

    c.append(t)

    return c

def a_poli(cadena):
    lista = __parsear_str(cadena)
    if lista[0][-1] == "X":
        grado = 1
    elif lista[0].isnumeric():
        grado = 0
    else:
        d = ""
        a = False
        for i in lista[0]:
            if a:
                d += i
            if i == "^":
                a = True

        grado = int(d)
    coeficientes = [0]*(grado + 1)
    for i in range(len(lista)-1,-1,-1):
        t: str = lista[i]
        coef: int = 0

        if t.isnumeric():
            coef = int(t)
            g = 0
        elif t != "+" and t != "-":
            c = ""
            if t[-1] == "X" or t[-1] == "x":
                g = 1
            else:
                d = ""
                a = False
                for k in t:
                    if a:
                        d += k
                    if k == "^":
                        a = True

                g = int(d)

            if t[0] == "X":
                c = "1"
            else:
                for j in t:
                    if j.isnumeric():
                        c+=j
                    else:
                        break

            coef = int(c)

        if i != len(lista) and lista[i-1] == "-":
            coef = -coef

        coeficientes[(-g) - 1] += coef


    return Polinomio(tuple(coeficientes))
