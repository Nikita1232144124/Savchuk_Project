#1

hat_list = [1, 2, 3, 4, 5]

new_number = int(input("Введіть ціле число для заміни: "))
hat_list[2] = new_number
hat_list.pop()
print("Довжина списку:",len(hat_list))
print(hat_list)

#2


n = int(input("Введіть кількість елементів у списку: "))
numbers = []
for i in range(n):
    num = int(input(f"Введіть {i+1}-й елемент: "))
    numbers.append(num)


flag = True
pass_num = 0
while flag:
    flag = False
    for i in range(len(numbers) - 1 - pass_num):
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
            flag = True
    pass_num += 1

print("Відсортований масив:", numbers)


#3

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
tempor = []

for num in my_list:
    if num not in tempor:
        tempor.append(num)

print("The list with unique elements only:")
print(tempor)

#4


chess_board = [["_"] * 8 for _ in range(8)]


chess_board[0][0] = "T"
chess_board[0][7] = "T"
chess_board[7][0] = "T"
chess_board[7][7] = "T"


for row in chess_board:
    print(" ".join(row))
