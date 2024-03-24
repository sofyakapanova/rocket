import turtle, time
t = turtle.Turtle()  # создали черепаху
t.shape('turtle')  # чтоб рисовала черепаха
t.speed(0)  # скорость с которой рисует черепаха
# корпус
t.color('black', 'grey')  # 1 цвет линий, 2 заливка
t.begin_fill()  # начинаем рисовать цветную фигуру
t.fd(100)  # вперед 100 пикс
t.left(90)  # поворот налево на 90 градусов
t.fd(250); t.lt(90); t.fd(100)
t.lt(90); t.fd(250); t.lt(90)
t.end_fill()  # заканчиваем рисовать цветную фигуру
# кабина
t.penup(); t.home(); t.pendown()
t.lt(90); t.fd(250); t.rt(90)
t.color('black', 'red')
t.begin_fill()
t.fd(100)
for i in range(2): t.lt(120); t.fd(100)
t.end_fill()
# левое крыло
t.penup(); t.home(); t.pendown()
t.color('black', 'green')
t.begin_fill()
t.lt(90); t.fd(100); t.lt(40); t.lt(90)
t.fd(100); t.lt(50); t.fd(150); t.lt(130)
t.fd(100); t.lt(50); t.fd(150)
t.end_fill()
# правое крыло
t.penup()
t.home()  # возвращаем перо в исходн полож-е
t.lt(90); t.fd(100); t.rt(90); t.fd(100)
t.pendown(); t.begin_fill()
t.rt(40); t.fd(100); t.rt(50); t.fd(150)
t.rt(130); t.fd(100); t.rt(50); t.fd(150)
t.end_fill()
# окно
t.penup(); t.home()
t.fd(50); t.lt(90); t.fd(100); t.rt(90)
t.width(10)  # как t.pensize(10) (толщина линии)
t.shapesize(3, 3, 2)  # размер черепахи
t.pendown(); t.color('black', 'cyan')
t.begin_fill()
t.circle(25)  # круг расдиусом 25 пикс
t.end_fill()

time.sleep(2)  # чтоб окно было видно 2 сек

# цвета можно занести в список и обращаться к его эл-м: colors = ['blue', 'black', 'red', 'yellow', 'green']; for i in range(3): t.pencolor(colors[i])
