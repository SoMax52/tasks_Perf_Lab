import sys

def array():
    # Ввод числа массива и её длины
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    l = list(range(1, n + 1))
    i = 0
    print("Результат: ", end="")
    # Вычисление кругового массива
    while True:
        print(l[i], end=" ")
        i = (i + m - 1) % n
        if i == 0:
            break

if __name__ == "__main__":
    array()
