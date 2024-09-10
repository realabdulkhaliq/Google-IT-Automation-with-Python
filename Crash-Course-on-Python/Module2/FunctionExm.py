def greeting(name):
    print("Hello, " + name)

greeting("AK")


def area_triangle(base, height):
    return base*height/2
area_a = area_triangle(5,4)
area_b = area_triangle(7,3)
sum = area_a + area_b
print("The sum of both areas is: " + str(sum))

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds
 
hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)

# Because we know that the function returns three values, 
# we assign the result of the function to three different variables.

def lucky_number(name):
    number = len(name) * 9
    print("Hello " + name + ". Your lucky number is " + str(number))

lucky_number("Kay")
lucky_number("Cameron")

def calculate(diameter):
    pi = 3.14
    circumfarance = pi * (diameter ** 2)
    print(circumfarance)

calculate(5)

def circle_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    print(area)

circle_area(5)