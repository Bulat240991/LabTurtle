import turtle
import time

print("Задача:\nНарисовать черепашкой выбранную фигуру\n"
      "Введите номер выбранной фигуры:\n"
      "1: Буква S\n"
      "2: Квадрат\n"
      "3: Круг\n"
      "4: Вложенные квадраты\n"
      "5: Звезда\n"
      "6: Спираль\n"
      "7: Квадратная 'спираль'\n"
      "8: Правильные многоугольники")

x = int(input())
elif x == 1:                   # Буква S
    turtle.shape('turtle')
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    time.sleep(3)

elif x == 2:                   # Квадрат
    turtle.shape('turtle')
    turtle.penup()
    turtle.goto(-75,75)
    turtle.pendown()
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    time.sleep(3)

elif x == 3:                  # Круг
    turtle.shape('turtle')
    y = 1
    while y < 360:
        turtle.forward(1)
        turtle.right(1)
        y += 1
    time.sleep(3)

elif x == 4:                  # Вложенные квадраты
    print("Сколько нарисовать квадратов:")
    y = int(input())        # Указываем колличество квадратов, которое будет нарисованно
    n = 20                  # Длинна грани первого квадрата в центре
    while y > 0:
        turtle.forward(n)
        turtle.right(90)
        turtle.forward(n)
        turtle.right(90)
        turtle.forward(n)
        turtle.right(90)
        turtle.forward(n)
        turtle.penup()      # По окончанию прорисовки пергого квадрата, смещаемя на позицию для прорисовки следующего
        turtle.left(90)
        turtle.forward(10)
        turtle.right(90)
        turtle.forward(10)
        turtle.right(90)
        turtle.pendown()
        n += 20             # Увеличиваем размер грани следущего квадрата
        y -= 1
        time.sleep(3)

elif x == 5:                   # Звевда
    print("Сколько лучей будет у звезды:")
    y = int(input())        # задаем колличество лучей
    z = 360/y
    while y > 0:
        turtle.shape('turtle')
        turtle.forward(100)
        turtle.stamp()
        turtle.backward(100)
        turtle.right(z)
        y -= 1
        time.sleep(3)

elif x ==6:                       # Спираль
    print("Введите число витков спирали")
    a = int(input())
    p = (a/2*3.14)*5
    for a in range(50):
        turtle.shape('turtle')
        turtle.forward(1)
        turtle.right(a)
        a += 1
        time.sleep(3)

elif x == 7:
    l = 5
    turtle.shape('turtle')
    while l < 100:
        turtle.forward(l)
        turtle.right(90)
        l += 5
        time.sleep(3)





