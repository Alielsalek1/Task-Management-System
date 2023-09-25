# a function to check if the input number is in range a minimum and a maximum value
def check_number_in_range(minimum, maximum):
    number = input(f"Enter a number in range {minimum} - {maximum}: ")

    while (not number.isdigit()) or int(number) > maximum or int(number) < maximum:
        number = input("Please Enter a valid number\n")

    return number

def main():
    pass

if __name__ == '__main__':
    main()