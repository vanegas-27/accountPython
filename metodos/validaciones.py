import re

# if len(idUser) < 10 or len(idUser) > 11:
#     print("I,m really sorry, your ID is NOT permitted, must be between 10 to 11 numbers.")

# if age < 18:
#     print("I,m really sorry, your age is NOT permitted, must be over 18.")

# if cash < 50.000:
#         print("I,m really sorry, your money is NOT permitted, must be over 50.000COP.")    

# if len(phone) != 10:
#     print("I'm very sorry, your number must be 10 to numbers.")

def validatedEmail(email) -> bool:
    # Expresión regular para validar el formato del email
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Verificar si el email coincide con el patrón
    if re.match(patron, email):
        return True
    
    return False



def typeValue(typeData, text):

    while True:
        try:
            value = typeData(input(text))
            return value
        except ValueError:
            print("This answer is NOT validated")
            continue



def validatedSavings(typeDate, date):
    while True:
        value = typeDate(input(date)).upper()

        if value == "NO":
            break
        elif value == "YES":
            savings = typeValue(float,"Enter your saving cant: ")
            if savings == 0:
                print("I'm really sorry, your savings cant is NOT permitted, must be over 0.0$")
                continue
            else:
                return savings
        else:
            print("This option is no validated.")
            continue


def __funcion():
    pass