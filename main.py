input_string = input('Введите значения длин сторон разделяя пробелом не больше 3х, если радиус - то одно значение:')
if input_string.replace(" ", "").isdigit():  # проверка на цифры
    values = input_string.split()
    count = len(values)
    if count <= 3:  # Проверка кол-ва сторон
        if count == 1:
            radius = int(input_string)
            if radius: # проверка на 0
                perimetr = 2 * 3.14 * radius
                sq = 3.14 * (radius * radius)
                print(
                    f'{"Круг:"} {"Радиус ="} {radius}; {"Площадь ="} {round(sq, 2)}, {"Периметр ="} {round(perimetr, 2)}')
            else:
                print(f' {"Круг не может быть с радиусом ="} {radius}')
        elif count == 2:
            a, b = values
            side_a = int(a)
            side_b = int(b)
            if side_a and side_b:  # проверка на 0
                perimetr = 2 * (side_a + side_b)
                sq = side_a * side_b
                if side_a == side_b:  # проверка на квадрат
                    type_str = 'Квадрат:'
                else:  # иначе прямоугольник
                    type_str = 'Прямоугольник:'
                print(f'{type_str} {"Сторона а ="} {side_a}, {"Сторона b ="} {side_b}; {"Площадь ="} {round(sq, 2)}, {"Периметр ="} {round(perimetr, 2)}')
            else:
                print(f'{"Фигуры со сторонами:"} {"a ="} {side_a} {"b ="} {side_b} {"не существует!"}')
        elif count == 3:
            a, b, c = values
            side_a = int(a)
            side_b = int(b)
            side_c = int(c)
            if side_a and side_b and side_c and side_a < side_c + side_b and side_b < side_a + side_c and side_c < side_a + side_b:  # проверка существования треугольника
                perimetr = side_a + side_b + side_c
                p_p = perimetr / 2
                sq = (p_p * ((p_p - side_a) * (p_p - side_b) * (p_p - side_c))) ** 0.5
                print(
                    f'{"Треугольник"}: {"сторона a ="} {side_a}, {"сторона b ="} {side_b}, {"сторона c ="} {side_c}; {"Площадь ="} {round(sq, 2)}, {"Периметр ="} {round(perimetr, 2)}')
            else:
                print(
                    f'{"Треугольника со сторонами:"} {"a ="} {side_a} {"b ="} {side_b} {"c ="} {side_c} {"- не существует!"}')
    else:
        print('Введено более 3х размеров сторон!')
else:
    print('Введены не корректные зачения!')