import math

def circle():
    # Ввод кординат центра окружности и её радиуса из файла circle.txt
    with open("circle.txt") as f:
        circ_x, circ_y = f.readline().split()
        rad = int(f.readline(2))
    circle_center_x = float(circ_x)
    circle_center_y = float(circ_y)
    radius = rad
    # Ввод координат точек X и Y из файла dot.txt
    with open("dot.txt") as f:
        points = f.readlines()
    for p in points:
        X = float(p.split()[0])
        Y = float(p.split()[1])
        # Вычисление расстояние между центром окружности и точкой
        distance = math.sqrt((circle_center_x - X) ** 2 + (circle_center_y - Y) ** 2)
        if distance < radius:
        # Точка внутри окружности
            print(1)
        elif distance == radius:
        # Точка лежит на окружности
            print(0)
        else:
        # Точка снаружи окружности
            print(2)

if __name__ == "__main__":
    circle()
