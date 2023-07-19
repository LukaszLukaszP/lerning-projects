
def sum_calculator(snum1, snum2):
    result = snum1 + snum2
    return result

def substraction(sub1, sub2):
    result = sub1 - sub2
    return result


def multiplication(mult1, mult2):
    result = mult1 * mult2
    return result

def division(div1, div2):
    result = div1 / div2
    return result

def keep_counting():
    #Ask the user if they want to continue or end counting
    response = input("Czy chcesz kontynuawać liczenie? Y/N")
    response = response.upper()
    while response not in ["Y", "N"]:
        response = input("Czy chcesz kontynuawać liczenie? Y/N")
    if response == "Y":
        return True
    elif response == "N":
        return False

def check_user_input(input):
    #checks whether the type of data entered by the user is correct (float)
    try:
        int(input)
        return False
    except ValueError:
        try:
            float(input)
            return False
        except ValueError:
            return True

def check_action(act):
    #check if the user action is a valid mathemaical operation
    actions = ["+", "-", "/", "*"]
    while act not in actions:
        return True
    return False

def division_zer_check(num):
    #check if the seconde number is zero and if it is ask user to enter a non-zero number
    while num == 0:
        print("Podaj liczbę różną od zera")
        num = enter_number()
    return num

def calculator(action, cal1, cal2):
    result = 0
    if action == "+":
        result = sum_calculator(cal1, cal2)
    elif action == "-":
        result = substraction(cal1, cal2)
    elif action == "*":
        result = multiplication(cal1, cal2)
    elif action == "/":
        cal2 = division_zer_check(cal2)
        result = division(cal1, cal2)
    return result

def choose_action():
    #asks user to choose a mathematical operation
    action = input("""Wybierz jakie działanie chcesz wykonać:
    + dodawanie
    - odejmowanie
    * mnożenie
    / dzielenie: """)

    while check_action(action):
        action = input("Podaj jakie działanie chcesz wykonać ( + - * / ): ")
    return action

def enter_number():
    #asks user to enter a number
    num = input("Podaj liczbę: ")
    while check_user_input(num):
        num = input("Podaj liczbę: ")
    num = float(num)
    return num

action = choose_action()

print("Podaj pierwszą liczbę")
num1= enter_number()

print("Podaj kolejną liczbę")
num2 = enter_number()

result = calculator(action, num1, num2)
print(result)

while keep_counting():
    action = choose_action()
    num1 = result
    print("Podaj kolejną liczbę")
    num2 = enter_number()
    result = calculator(action, num1, num2)
    print(result)
