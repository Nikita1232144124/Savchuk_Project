#1

import math

x = 1.5
mu = 2.0
sigma = 0.5
result = 1 / (sigma * math.sqrt(2 * math.pi))-((x - mu) ** 2) / (2 * (sigma ** 2))
print("f(x)=",result)


#2


john=3
mary=5
adam=6
print(john,mary,adam,sep=",")
totalapples=john+mary+adam
print(totalapples)
print("Загальна кількість яблук:",totalapples)


#3


kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

#4

x = -1
x = float(x)
y = 3*x**3-2*x**2+3*x-1
print("y =", y)


#5

# this program computes the number of seconds in a given number of hours

hours = 2 # number of hours
seconds = 3600 # number of seconds in 1 hour

print("Hours: ", hours)
print("Seconds in Hours: ", hours * seconds) # printing the number of seconds in a given number of hours

#this is the end of the program that computes the number of seconds in 2 hour

#6

a = 1.5
b = 16.2

print("addition:",a+b)
print("subtraction:",a-b)
print("multiplication:",a*b)
print("division:",a/b)

print("\nThat's all, folks!")

#7

x = float(input("Enter value for x: "))

y=1/(x + (1 / (x + (1 / (x + (1 / (x + (1 / x))))))))

print("y =", y)

#8

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

min_result= (mins+dura)%60
hour_result=(hour+(mins+dura)//60)%24

print(hour_result,min_result,sep=":")