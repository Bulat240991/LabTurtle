import turtle
import time

print("Задача:\nНарисовать черепашкой выбранную фигуру\n"
      "Введите номер выбранной фигуры:\n"
      "1: Буква S\n"
      "2: Квадрат\n"
      "3: Круг\n"
      "4: Пирамида\n"
      "5: Звезда\n"
      "6: Спираль\n"
      "7: Квадратная 'спираль'\n"
      "8: Правильные многоугольники")

x = int(input())
if x == 1                   # Буква S
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

if x == 2:                   # Квадрат
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

if x == 3:                  # Круг
    y = 1
    while y < 360:
        turtle.forward(1)
        turtle.right(1)
        y += 1
    time.sleep(3)

