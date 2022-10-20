input_string = input('Введите значения длин сторон разделяя пробелом не больше 3х, если радиус - то одно значение:')
if input_string.replace(" ", "").isdigit(): # проверка на цифры
    values = input_string.split()
    count = len(values)
    if count <= 3:  # Проверка кол-ва сторон
        perim_str = 'Периметр = '
        squere_str = 'Площадь = '
        side_a_str = 'Сторона a = '
        side_b_str = 'Сторона b = '
        side_c_str = 'Сторона c = '
        if count == 1:
            if int(input_string):  # проверка на 0
                type_str = 'Круг:'
                rad_str = 'Радиус = '
                radius = int(input_string)
                perimetr = 2 * 3.14 * radius
                sq = 3.14 * (radius * radius)
                print(f'{type_str} {rad_str} {radius}; {perim_str} {round(perimetr, 2)}, {squere_str} {round(sq, 2)}')
            else:
                print('Введен "0"')
        elif count == 2:
            a, b = values
            if int(a) and int(b):  # проверка на 0
                side_a = int(a)
                side_b = int(b)
                if side_a == side_b: #проверка на квадрат
                    type_str = 'Квадрат:'
                    perimetr = 4 * side_a
                    sq = side_a * side_a
                    print(f'{type_str} {side_a_str} {side_a}; {perim_str} {round(perimetr, 2)}, {squere_str} {round(sq, 2)}')
                else: # иначе прямоугольник
                    type_str = 'Прямоугольник:'
                    perimetr = 2 * (side_a + side_b)
                    sq = side_a * side_b
                    print(
                        f'{type_str} {side_a_str} {side_a}, {side_b_str} {side_b}; {perim_str} {round(perimetr, 2)}, {squere_str} {round(sq, 2)}')
            else:
                print('Введен "0"')
        elif count == 3:
            a, b, c = values
            if int(a) and int(b) and int(c): # проверка на 0
                if int(a) < int(c) + int(b) and int(b) < int(a) + int(c) and int(c) < int(a) + int(b):  # проверка существования треугольника
                    side_a = int(a)
                    side_b = int(b)
                    side_c = int(c)
                    type_str = 'Треугольник:'
                    perimetr = side_a + side_b + side_c
                    p_p = perimetr / 2
                    sq = (p_p * ((p_p - side_a) * (p_p - side_b) * (p_p - side_c))) ** 0.5
                    print(
                        f'{type_str} {side_a_str} {side_a}, {side_b_str} {side_b}, {side_c_str} {side_c}; {perim_str} {round(perimetr, 2)}, {squere_str} {round(sq, 2)}')
                else:
                    print('Треугольника с такими сторонами не существует!')
            else:
                print('Введен "0"')
    else:
        print('Введено более 3х размеров сторон!')
else:
    print('Введены не корректные зачения!')