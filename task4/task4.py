import sys

def step():
    # Ввод данных из файла numbers.txt
    p_nums = sys.argv[1]
    with open(p_nums) as f:
        nums = f.readlines()
        numbers = [int(i) for i in nums]
    numbers.sort()
    # Вычисление суммы среднего числа
    x = len(numbers) // 2
    avg = sum(abs(n - numbers[x]) for n in numbers)
    print(avg)
        
if __name__ == '__main__':
    step()
