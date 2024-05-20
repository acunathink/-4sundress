need_nums: str = input("Введите количество элементов: ")
while not need_nums.isdigit():
    need_nums: str = input("Введите только число: ")
sequence: list[str] = []
for num in range(1, int(need_nums) + 1):
    sequence.append(str(num) * num)
print("".join(sequence))
