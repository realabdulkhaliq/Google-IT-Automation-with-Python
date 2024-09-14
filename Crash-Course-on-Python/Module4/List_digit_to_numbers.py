1 == "one"
2 == "two"
3 == "three"
4 == "four"
5 == "five"
6 == "six"
7 == "seven"
8 == "eight"
9 == "nine"
10 == "ten"
20 == "twenty"
30 == "thirty"
40 == "forty"
50 == "fifty"
60 == "sixty"
70 == "seventy"
80 == "eighty"
90 == "ninety"
100 == "hundred"



def find_numbers(numbers):
    for number in numbers.split():
        if number == "one":
            print(1)
        elif number == "two":
            print(2)
        elif number == "three":
            print(3)
        elif number == "four":
            print(4)
        elif number == "five":
            print(5)
        elif number == "six":
            print(6)
        elif number == "seven":
            print(7)
        elif number == "eight":
            print(8)
        elif number == "nine":
            print(9)
        elif number == "ten":
            print(10)
        elif number == "twenty":
            print(20)
        elif number == "thirty":
            print(30)
        elif number == "forty":
            print(40)
        elif number == "fifty":
            print(50)
        elif number == "sixty":
            print(60)
        elif number == "seventy":
            print(70)
        elif number == "eighty":
            print(80)
        elif number == "ninety":
            print(90)
        elif number == "hundred":
            print(100)
        else:
            print("Invalid number")

print(find_numbers("sixty seven"))