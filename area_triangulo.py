def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

base = float(input('Introduzca el área de la base: '))
altura = float(input('Introduzca el área de la altura: '))

print('El área del triángulo es: ', area_triangulo(base, altura))

# Ejercicio 2

def area_circulo(radio):
    area_total_circulo = 3.14 * (radio ** 2)
    return area_total_circulo

radio = float(input('Introduzca el radio del círculo: '))
print('El área del círculo es: ', area_circulo(radio))

