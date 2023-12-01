#1

# n = int(input("Введіть ціле число n: "))
# print(n >= 100)
#
# #2
#
#
# num1 = float(input("Введіть перше  число: "))
# num2 = float(input("Введіть друге  число: "))
#
# if num1 > num2:
#     max_number = num1
# else:
#     max_number = num2
#
# print("Найбільше число:", max_number)
#
#
# #3
#
# plant = input("Введіть назву рослини: ")
# if plant == "spathiphyllum":
#     print("No, I want a big Spathiphyllum!")
# elif plant == "pelargonium":
#     print("Spathiphyllum! Not pelargonium!")
# elif plant == "Spathiphyllum":
#     print("Yes - Spathiphyllum is the best plant ever!")
# else:
#     print("Неправильний ввід")
#
# #4
#
# income = float(input("Enter the annual income: "))
#
# if income <= 85528:
#     tax = income * 0.18 - 556.02
# else:
#     tax = 14839.02 + (income - 85528) * 0.32
#
# if tax <= 0:
#     tax = 0
#
# tax = round(tax, 0)
# print("The tax is:", tax, "thalers")
#
#
# #5
#
# year = int(input("Введіть рік: "))
#
# if year < 1582:
#     print("Not within the Gregorian calendar period")
# else:
#     if year % 4 != 0:
#         print("Common year")
#     elif year % 100 != 0:
#         print("Leap year")
#     elif year % 400 != 0:
#         print("Common year")
#     else:
#         print("Leap year")
#
# #6
#
# secret_number = 777
#
# print(
# """
# +================================+
# | Welcome to my game, muggle!    |
# | Enter an integer number        |
# | and guess what number I've     |
# | picked for you.                |
# | So, what is the secret number? |
# +================================+
# """)
#
# while True:
#     user_number = int(input("Введіть ціле число: "))
#
#     if user_number == secret_number:
#         print("Молодець, магле! Тепер ти вільний")
#         break
#     else:
#         print("Ха-ха! Ви застрягли у моїй петлі! Спробуйте ще раз.")
#
# #7
#
# import time
#
# for i in range(1, 6):
#     print(i, "Міссісіпі")
#     time.sleep(1)
#
# print("Ready or not, here I come!")
#
# #8
#
# while True:
#     word = input("Введіть слово: ")
#     if word.lower() == "chupacabra":
#         break
#
# print("You've successfully left the loop.")
#
#
# #9
#
# user_word = input("Введіть слово: ")
# user_word = user_word.upper()
#
# for letter in user_word:
#     if letter in ['A', 'E', 'I', 'O', 'U']:
#         continue
#     print(letter)
#
#
# #10
#
# word_without_vowels = ""
# user_word = input("Введіть слово: ")
# user_word = user_word.upper()
#
# for letter in user_word:
#     if letter in ['A', 'E', 'I', 'O', 'U']:
#         continue
#     word_without_vowels += letter
#
# print(word_without_vowels)
#
#
# #11
#
# blocks = int(input("Введіть кількість блоків: "))
# height = 0
# count = 0
#
# while count < blocks:
#     height += 1
#     count += height
#
# if count > blocks:
#     height -= 1
#
# print("The height of the pyramid:", height)
#

#12

c0 = int(input("Введіть натуральне число: "))
steps = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 //= 2
    else:
        c0 = 3 * c0 + 1
    print(c0)
    steps += 1

print(c0)
print(f"Кількість кроків: {steps}")
