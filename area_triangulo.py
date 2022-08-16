def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

base = float(input('Introduzca el área de la base: '))
altura = float(input('Introduzca el área de la altura: '))

print('El área del triángulo es: ', area_triangulo(base, altura))

