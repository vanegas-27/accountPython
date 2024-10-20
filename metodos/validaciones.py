import re

## validacion de email
def __validatedEmail(email) -> bool:
    # Expresión regular para validar el formato del email
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Verificar si el email coincide con el patrón
    if re.match(patron, email):
        return email
    
    print("This email is NOT validated")
    return False

## verificacion de saldo de ahorros
def validatedSavings(typeDate, date):
    while True:
        value = typeDate(input(date)).upper()

        if value == "NO":
            break
        elif value == "YES":
            savings = validatedValue(float,"Enter your saving cant: ")
            if savings == 0:
                print("I'm really sorry, your savings cant is NOT permitted, must be over 0.0$")
                continue
            else:
                return savings
        else:
            print("This option is no validated.")
            continue



## condicionales
def __verificIdUser(__idUser : int) -> bool:
    if len(str(__idUser)) < 10 or len(str(__idUser)) > 11:
        print("I,m really sorry, your ID is NOT permitted, must be between 10 to 11 numbers.")
        return False
    return True

def __verificAge(__age : int) -> bool:
    if __age < 18:
        print("I,m really sorry, your age is NOT permitted, must be over 18.")
        return False
    return True

def __verificCash(__cash :float) -> bool:
    if __cash < 50.000:
        print("I,m really sorry, your money is NOT permitted, must be over 50.000COP.") 
        return False
    return True
              
def __verificPhone(__phone : int) -> bool:
    if len(str(__phone)) != 10:
        print("I'm very sorry, your number must be 10 to numbers.")
        return False
    return True


def validatedValue(typeData, text, verific = None):

    verifications = {
        "id" : __verificIdUser,
        "age" : __verificAge,
        "cash" : __verificCash,
        "phone" : __verificPhone,
        "email" : __validatedEmail
    }

    while True:
        try:
            value = typeData(input(text))
            if verific != None:
                if not verifications[verific](value):
                    continue
                else:
                    return value
            return value
        except ValueError:
            print("This answer is NOT validated")
            continue

