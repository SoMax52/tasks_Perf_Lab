import sys
import math

def circle():
    # Ввод кординат центра окружности и её радиуса из файла circle.txt
    circle_file = sys.argv[1]
    with open(circle_file) as f:
        circ_x, circ_y = f.readline().split()
        circ_x, circ_y = float(circ_x), float(circ_y)
        rad = int(f.readline(2))
    # Ввод координат точек X и Y из файла dot.txt
    dot_file = sys.argv[2]
    with open(dot_file) as f:
        points = f.readlines()
    for p in points:
        X, Y = float(p.split()[0]), float(p.split()[1])
        # Вычисление расстояние между центром окружности и точкой
        dist = math.sqrt((circ_x - X) ** 2 + (circ_y - Y) ** 2)
        if dist < rad:
        # Точка внутри окружности
            print(1)
        elif dist == rad:
        # Точка лежит на окружности
            print(0)
        else:
        # Точка снаружи окружности
            print(2)

if __name__ == "__main__":
    circle()
