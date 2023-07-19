
def hp_to_kw(hp):
    kw = hp * 1.34
    return kw

def kw_to_hp(kw):
    hp = kw /1.34
    return hp

def celsius_to_farenheit(celc):
    faren = (celc * 9 / 5) + 32
    return faren

def farenheit_to_celsius(faren):
    celc = (faren - 32) * 5 / 9
    return celc

def check_user_input(value):
    try:
        int(value)
        return False
    except ValueError:
        try:
            float(value)
            return False
        except ValueError:
            return True

choose = input("1 - hp to kw\n2 - kw to hp\n3 - celsius to farenheit\n4 farenheit to celsius")
value = input("Enter value to convert: ")
while check_user_input(value):
    value = input("Enter value to convert: ")
value = float(value)

if choose == "1":
    print(str(value), "hp", "=", hp_to_kw(value), "kw")
elif choose == "2":
    print(str(value), "kw", "=", kw_to_hp(value), "hp")
elif choose == "3":
    print(str(value), "C", "=", celsius_to_farenheit(value), "F")
elif choose == "4":
    print(str(value), "F", "=", farenheit_to_celsius(value), "C")