#1

def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")


2

def is_year_leap(year):

    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):

    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month < 1 or month > 12 or year < 1:
        return None
    if is_year_leap(year):
        days_in_months[1] = 29
    return days_in_months[month - 1]

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

#3

def is_year_leap(year):

    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):

    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month < 1 or month > 12 or year < 1:
        return None
    if is_year_leap(year):
        days_in_months[1] = 29
    return days_in_months[month - 1]

def day_of_year(year, month, day):

    if not is_year_leap(year) and month == 2 and day > 28:
        return None

    days = days_in_month(year, month)
    if days is None or day < 1 or day > days:
        return None

    day_number = sum(days_in_month(year, m) for m in range(1, month)) + day
    return day_number


print(day_of_year(2000, 12, 31))
print(day_of_year(2008, 10, 14))
print(day_of_year(2024, 5, 20))

#4


def is_prime(num):
    if num <= 1:
        return False


    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


for i in range(1, 20):
    if is_prime(i + 1):
            print(i + 1, end=" ")
print()

#5

def liters_100km_to_miles_gallon(liters):
    miles = 100 / (liters / 3.785411784 * 1.609344)
    return miles

def miles_gallon_to_liters_100km(miles):
    liters = 100 / (miles * 1.609344 / 3.785411784)
    return liters


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

#6

def is_a_triangle(a, b, c):

    return (a + b > c) and (b + c > a) and (a + c > b)


print(is_a_triangle(3, 4, 5))
print(is_a_triangle(1, 1, 4))
print(is_a_triangle(2, 6, 10))


def is_a_right_triangle(a, b, c):

    if is_a_triangle(a, b, c):

        hypotenuse = max(a, b, c)

        squares_sum = 0
        if hypotenuse == a:
            squares_sum = b ** 2 + c ** 2
        elif hypotenuse == b:
            squares_sum = a ** 2 + c ** 2
        else:
            squares_sum = a ** 2 + b ** 2

        if hypotenuse ** 2 == squares_sum:
            return True

    return

print(is_a_right_triangle(3, 4, 5))
print(is_a_right_triangle(1, 1, 4))
print(is_a_right_triangle(2, 6, 10))