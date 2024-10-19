from clases.clase_cuenta import Cuenta
from metodos.validaciones import validatedEmail, validatedSavings, typeValue


def crearCuenta() -> None:

    idUser = typeValue(int,"Enter your ID: ")
    name = typeValue(str,"Enter your full name: ")
    age = typeValue(int,"Enter your age: ")
    cash = typeValue(float,"Enter your full total money(MIN 50COP): ")
    adress = typeValue(str,"Enter your address: ")
    phone = typeValue(int,"Enter your number phone: ")
    email = typeValue(str,"Enter your email: ")
    if not validatedEmail(email):
        print("This email is NOT validated")
        return
    savings = validatedSavings(str, "Do you want to deposit to the savings account? YES/NO: ") or 0.0
    DATA = [idUser, name, age, cash, adress, phone, email, savings]





def verCuenta() -> None:
    pass

def moverAhorros() -> None:
    pass


def moverCuenta() -> None:
    pass

def retiarSaldo() -> None:
    pass

def enviarDinero() -> None:
    pass

def cambiarSucursal() -> None:
    pass

def verMovimientos() -> None:
    pass