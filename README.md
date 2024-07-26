# pypoly
Python library for managing polynomials

Hola! Bienvenido a Polinomios, el notebook que te permitirá hacer cuentas con polinomios (dividir, multiplicar, sumar, restar, hallar el resto) y muchas cosas más!

***Nota: Para poder usar este notebook tenés que apretar el simbolito de "Play" a la izquierda del código de abajo. Eso ejecuta el código.***

Comencemos:

# Inicialización:

La forma de trabajar con la clase es creando objetos **Polinomio** que se pueden crear de dos maneras distintas. Una es utilizando el inicializador ```Polinomio()``` que toma una tupla de números reales que serán los **coeficientes** del polinomio. Por ejemplo, la siguiente entrada crea el polinomio $f = x^2 - 1$:

```
f = Polinomio(1,0,-1)
```

Representamos a $x^2 - 1$ como $1x^2 + 0x - 1$. Más específicamente la posición $i$ de la tupla representa al coeficiente de grado $gr(f) - i$.

Así se inicializaría el polinomio $g = 3x^4 + 2x^3 - x$:

```
g = Polinomio(3,2,0,-1,0)
```

La otra forma de crear objetos Polinomio es a través de la función ```a_poli(cadena)``` que toma una cadena con formato

$a_1x^n \pm\ a_2x^{n-1} \pm\ \ldots\ \pm\ a_{n-1}x \pm\ a_n$

con $a_1, a_2, \ldots\ , a_n$ reales positivos.

Por ejemplo así se crea con este formato el polinomio $f = 2x^4 - 1$



```
f = a_poli("2X^4 - 1")
```

# Operaciones básicas:

Los polinomios se pueden sumar, restar, multiplicar y dividir usando los operadores normales de python.


```
f = Polinomio(1, 0, 2, -1)
g = Polinomio(2, -3)
print(f + g)

#Output: "X^3 + 4X - 4"

```
```
f = Polinomio(1, 0, 2, -1)
g = Polinomio(2, -3)
print(f - g)

#Output: "X^3 + 2"

```
```
f = Polinomio(1, 0, 2, -1)
g = Polinomio(2, -3)
print(f * g)

#Output: "2X^4 - 3X^3 + 4X^2 - 8X + 3"

```
```
f = Polinomio(1, 0, 2, -1)
g = Polinomio(2, -3)
print(f / g)

#Output: "0.5X^2 + 0.75X + 2.125"
(Cociente sin resto)

```

También se puede hallar el resto en la división con el operador '```%```':
```
f = Polinomio(1, 0, 2, -1)
g = Polinomio(2, 1, -3)
print(f % g)

#Output: "3.75X - 1.75"
```

Para realizar operaciones con números es necesario inicializar a los mismos como polinomios:

```
f = Polinomio(1, 0, 2, -1)

print(f + 2)

#Tira error!!

#La sintaxis correcta es:

print(f + Polinomio(2))

#Output: "X^3 + 2X + 1"
```

# Funciones y métodos:

Como ya vimos, los objetos ```Polinomio```se puede imprimir por pantalla utilizando la función ```print()```.

También existen las siguientes funciones y métodos:

**mcd()**:

Devuelve el Mayor Común Divisor entre dos polinomios:

```
f = a_poli("2X^5 + X^4 + X^3 - 7X + 3")
g = a_poli("2X^3 - X^2 - 4X + 3")

print(mcd(f, g))

#Output: "4.0X^2 + 2.0X - 6.0"
```

**.copy()**:

Devuelve una copia del objeto Polinomio:

```
f = Polinomio(1,1)
g = f.copy()

print(g)

#Output: "X + 1"
```

**.grado()**:

Devuelve el grado del polinomio:

```
f = Polinomio(1,2,0,5,2)

print(f.grado())

#Output: 4
```

**a_poli(cadena: str)**:

Ya documentada.

# Próximamente:

**.graph()**

**.raices()**

**.eval()**

# A codear.

Acá abajo está el código. Podés copiar este notebook, copiarte el código en tu VS code, no sé lo que quieras. También podés escribir nuevas celdas en este mismo notebook. Tranqui que no va a afectar el código! :)


# Hay más?

Lo que vos quieras agregar! Calcular raíces, generar la función f(x), graficar, derivar, etc. Algunas cosas sé como hacerlas, otras no.

Todavía estoy viendo como hacerlo más colaborativo... pero cualquier cosa escribime a mi mail pedrovicente2709@gmail.com

Espero que sea útil!
Saludos,
Pedro.
