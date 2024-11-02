from clases.clase_cuenta import Cuenta
import metodos.validaciones as mt
import persistencia.persistencia as pt
import bcrypt


def crearCuenta() -> None:

    idUser = mt.validatedValue(int,"Enter your ID: ","id")
    name = mt.validatedValue(str,"Enter your full name: ")
    age = mt.validatedValue(int,"Enter your age: ","age")
    password = mt.validatedValue(str,"Enter your password: ")
    cash = mt.validatedValue(float,"Enter your full total money(MIN 50COP): ","cash")
    address = mt.validatedValue(str,"Enter your address: ")
    phone = mt.validatedValue(int,"Enter your number phone: ","phone") 
    email = mt.validatedValue(str,"Enter your email: ","email")
    savings = mt.validatedSavings(str, "Do you want to deposit to the savings account? YES/NO: ") or 0.0


    password_encode = f"{password}".encode('utf-8') 
    hashPassword = bcrypt.hashpw(password_encode, bcrypt.gensalt(10))

    account = Cuenta({
        "id" : idUser,
        "name" : name,
        "age" : age,
        "cash" : cash,
        "address" : address,
        "phone" : phone,
        "email" : email,
        "savings" : savings,
        "password" : hashPassword
    })
    location = account.getLocation()

    DATA = [idUser, name, age, cash, address, phone, email, location, savings, hashPassword]

    pt.createUser("INSERT INTO `usuarios` (`id`, `name`, `age`, `cash`, `address`, `phone`, `email`, `location`, `ahorros`, `password`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",DATA)




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