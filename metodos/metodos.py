from clases.clase_cuenta import Cuenta
import metodos.validaciones as mt

__CUENTAS = []

def crearCuenta() -> None:

    idUser = mt.validatedValue(int,"Enter your ID: ","id")
    name = mt.validatedValue(str,"Enter your full name: ")
    age = mt.validatedValue(int,"Enter your age: ","age")  
    cash = mt.validatedValue(float,"Enter your full total money(MIN 50COP): ","cash")
    address = mt.validatedValue(str,"Enter your address: ")
    phone = mt.validatedValue(int,"Enter your number phone: ","phone") 
    email = mt.validatedValue(str,"Enter your email: ","email")
    savings = mt.validatedSavings(str, "Do you want to deposit to the savings account? YES/NO: ") or 0.0

    persona = Cuenta({
        "id" : idUser,
        "name" : name,
        "age" : age,
        "cash" : cash,
        "address" : address,
        "phone" : phone,
        "email" : email,
        "savings" : savings,
    })

    __CUENTAS.append({persona.getId() : persona})






def verCuenta() -> None:
    for i in __CUENTAS:
        print(i)

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