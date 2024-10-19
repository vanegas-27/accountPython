
def main() -> str:
    return f'''
-- -- -- CUENTAS BANCARIAS DEVANEGAS -- -- --
      ---------------------------------
    Este software fue creado con la intencion
    de practicar los fundamentos de python y
    aplicarlos en un ejercicio que sume todas
    o gran parte de ellas. 
      
    Crea tu cuenta ya.!!
'''
if __name__ == "__main__":
    import metodos.metodos as mt

    # asignamos cada metodo a su correspondiente opcion
    __METODOS = {
        1 : mt.crearCuenta,
        2 : mt.verCuenta,
        3 : mt.moverAhorros,
        4 : mt.moverCuenta,
        5 : mt.retiarSaldo,
        6 : mt.enviarDinero,
        7 : mt.cambiarSucursal,
        8 : mt.verMovimientos,
    }

    # texto por defecto del menu 
    __DEFAULT = '''
        ------------------OPCIONES-----------
    1: CREAR ACCOUNT.
    2: VIEW ACCOUNT DATA.
    3: MOVE MONEY TO SAVING.
    4: MOVE MONEY TO ACCOUNT.
    5: WITHDRAW MONEY THE ACCOUNT.
    6: SEND MONEY TO ANOTHER ACCOUNT.
    7: CHANGE LOCATION TO SUCURSAL.
    8: SEE MOVEMENT ACCOUNT.

    0: EXIT.
        -------------------------------------
    '''
    print(main())

    while True:

        print(__DEFAULT)

        try:
            inputUser = int(input("Enter your option number: "))
        except ValueError:
            print("I'm really sorry, NO is allo characters. only number.")

        if(inputUser == 0):
            break

        if inputUser in __METODOS.keys():
            __METODOS[int(inputUser)]()
        else:
            print("i'm really sorry, this option NO in the list.")
    
    print("Chao Chaooo. VUELVE PRONTO.!!!")
