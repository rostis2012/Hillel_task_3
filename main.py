input_string = input('Введите значения длин сторон разделяя пробелом не больше 3х, если радиус - то одно значение:')
values = input_string.split()

# проверка на наличие символов и букв
if ''.join(values).isdigit() != True:
    print('Введите цифровые значения сторон! Буквы и спецсимволы недопустимы!')
    quit()

# проверить наличие 0, без знания цикла, на этапе ввода не вижу возможным

count = len(values)
if count <= 3:  # Проверка кол-ва сторон
    perim_str = 'Периметр = '
    squere_str = 'Площадь = '
    side_a_str = 'Сторона a = '
    side_b_str = 'Сторона b = '
    side_c_str = 'Сторона c = '
    if count == 1:
        if int(input_string) == 0:  # проверка на 0
            print('Введен "0"! Будьте внимательны!')
            quit()
        type_str = 'Круг:'
        rad_str = 'Радиус = '
        radius = int(input_string)
        perimetr = 2 * 3.14 * radius
        sq = 3.14 * (radius * radius)
        print(f'{type_str} {rad_str} {radius}; {perim_str} {round(perimetr, 2)}, {squere_str} {round(sq, 2)}')
    elif count == 2:
        a, b = values
        side_a = int(a)
        side_b = int(b)
        if side_a == 0 or side_b == 0:  # проверка на 0
            print('Введен "0"! Будьте внимательны!')
            quit()
        if side_a == side_b:
            type_str = 'Квадрат:'
            perimetr = 4 * side_a
            sq = side_a * side_a
            print(f'{type_str} {side_a_str} {side_a}; {perim_str} {round(perimetr, 2)}, {squere_str} {round(sq, 2)}')
        else:
            type_str = 'Прямоугольник:'
            perimetr = 2 * (side_a + side_b)
            sq = side_a * side_b
            print(
                f'{type_str} {side_a_str} {side_a}, {side_b_str} {side_b}; {perim_str} {round(perimetr, 2)}, {squere_str} {round(sq, 2)}')
    elif count == 3:
        a, b, c = values
        side_a = int(a)
        side_b = int(b)
        side_c = int(c)
        if side_a == 0 or side_b == 0 or side_c == 0:  # проверка на 0
            print('Введен "0"! Будьте внимательны!')
            quit()
        if side_a < side_c + side_b and side_b < side_a + side_c and side_c < side_a + side_b:  # проверка существования треугольника
            type_str = 'Треугольник:'
            perimetr = side_a + side_b + side_c
            p_p = perimetr / 2
            sq = (p_p * ((p_p - side_a) * (p_p - side_b) * (p_p - side_c))) ** 0.5
            print(
                f'{type_str} {side_a_str} {side_a}, {side_b_str} {side_b}, {side_c_str} {side_c}; {perim_str} {round(perimetr, 2)}, {squere_str} {round(sq, 2)}')
        else:
            print('Треугольника с такими сторонами не существует!')
            quit()
else:
    print('Введено более 3х размеров сторон!')
    quit()