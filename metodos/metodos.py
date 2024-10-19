from clases.clase_cuenta import Cuenta
from metodos.validaciones import validatedEmail, validatedSavings, validatedValue


def crearCuenta() -> None:

    idUser = validatedValue(int,"Enter your ID: ")
    name = validatedValue(str,"Enter your full name: ")
    age = validatedValue(int,"Enter your age: ")
    cash = validatedValue(float,"Enter your full total money(MIN 50COP): ")
    adress = validatedValue(str,"Enter your address: ")
    phone = validatedValue(int,"Enter your number phone: ")
    email = validatedValue(str,"Enter your email: ")
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