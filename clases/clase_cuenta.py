import random
import datetime as dt
from typing import List, Dict, Union


#crear la clase Cuenta
class Cuenta:

    # variable que guarda el tiempo de la moficicacion de location
    __timeLocations = {}

    # cosntante que almacena los movimientos de la cuenta
    __MOVIMIENTOS = []

    # lista consntante de las ubicacaiones validas.
    __LOCATIONS = [
        "medellin",
        "sabaneta",
        "envigado",
        "itagui",
        "bello",
        "copacabana"
    ]
    

    def __init__(self, dic:Dict[str , Union[str , int, float]]) -> None:
        '''
            ### funcion inicializadora de las variables, recibe los siguientes parametros.

            id(obligarorio) -> numero de cuenta.

            name(obligarorio) -> nombre de la persona.

            cash(obligarorio) -> dinero inicial de cuenta

            age(obligarorio) -> edad de persona

            address(obligarorio) -> direccion de la persona

            phone(obligarorio) -> telefono de la persona

            email(obligarorio) -> email de contacto

            ahorros(opcional) -> valor de ahorros si desea ingresar a la cuenta

            location -> este se crea aleatorio

            @return None
        '''
    
        self.__id = dic["id"]
        self.__name = dic["name"]
        self.__cash = dic["cash"]
        self.__age = dic["age"]
        self.__address = dic["address"]
        self.__phone = dic["phone"]
        self.__email = dic["email"]
        self.__savings = dic["savings"]
        self.__location = self.__LOCATIONS[random.randint(0, len(self.__LOCATIONS) - 1)]
        self.__password = dic["password"]



    # metodo str, describe la cuenta con los datos de la misma
    def __str__(self) -> str:
        return f"""
--- ACCOUNT DATA WITH ID:{self.__id} ---
> Name : {self.__name}
> Age : {self.__age}
> Phone : {self.__phone}
> Address : {self.__address}
> Email : {self.__email}
> Location : {self.__location}
------------------------------
-> Savings : {self.__savings}
-> Cash : {self.__cash} 
"""

    
    #Getters, encargados de devolver el valor de los atributos
    def getId(self) -> int:
        return self.__id
    
    def getName(self) -> str:
        return self.__name
    
    def getCash(self) -> float:
        return self.__cash
    
    def getAge(self) -> int:
        return self.__age
    
    def getAddress(self) -> str:
        return self.__address
    
    def getPhone(self) -> str:
        return self.__phone
    
    def getEmail(self) -> str:
        return self.__email
    
    def getLocation(self) -> str:
        return self.__location
    
    def getMovimientos(self) -> List[Dict[str,str]]:
        return self.__MOVIMIENTOS
    
    def getAhorros(self) -> list:
        return self.__savings


    # Setters, encargados de modificar el estado de los atributos
    def setId(self, id:int) -> None:
        self.__id = id

    def setName(self, name:str) -> None:
        self.__name = name
        
    def setCash(self, cash:float) -> None:
        self.__cash = cash

    def setAge(self, age:int) -> None:
        self.__age = age

    def setAddress(self, address:str) -> None:
        self.__address = address
    
    def setPhone(self, phone:str) -> None:
        self.__phone = phone
    
    def setEmail(self, email:str) -> None:
        self.__email = email

    def setMoviemientos(self, dates:dict) -> None:
        self.__MOVIMIENTOS.append(dates)

    def setAhorros(self,cash:float) -> None:
        self.__savings = cash

    

    def transferAhorros(self, cant:float, dates:dict) -> bool:
        '''
        ### Funcion encargada de enviar el dinero de la cuenta al dinero de ahorros, recibe los parametros:

        cant -> cantidad de dinero que se movera
        dates -> datos del movimiento para guardarlo en el log

        @return bool
        '''
        if self.__cash < cant:
            return False
        
        self.__savings += cant
        self.__cash -= cant
        self.setMoviemientos(dates)
        return True

    
    def transferCash(self, cant:float, dates:dict) -> bool:
        '''
        ### Funcion encargada de enviar el dinero de ahorros. a la cuenta convicional, recibe los parametros:

        cant -> cantidad de dinero que se movera
        dates -> datos del movimiento para guardarlo en el log

        @return bool
        '''
        if self.__savings < cant:
            return False
        
        self.__cash += cant
        self.__savings -= cant
        self.setMoviemientos(dates)
        return True


    #cambiar de sucursal
    def updateLocation(self, location:str, dates:dict) -> None:
        '''
        ### funcion encargada de gestionar la modificacion de la localizacion que le toco a la cuenta, recibe los parametros:

        location -> ubicacion donde desea ser trasnladado

        dates -> datos del traslado para guardar en el log

        @return None
        '''

        try:

            #preguntamos si la sucursal ya esta asignada
            if location.lower() == self.__location:
                print(f"Ya estas en la sucursal {location}. intenta con otra u omite este mensaje")
                return
            
            # verifica la existencia de la ubicacion en la lista. devuelve un boleano
            exist = location.lower() in self.__LOCATIONS

            #preguntamos si existe la sucursal en la lista y si no se ah realizado cambios creamos una modificacion de cero
            if  exist and len(self.__timeLocations.keys()) < 1:
                time = dt.datetime.now()
                self.__timeLocations = {
                    "dateCompled" : time,
                    "date": time.strftime("%x"),
                    "hour": time.strftime("%X")
                }

                self.__location = location
                self.setMoviemientos(dates)
                return
            
            # si ya existio una modificacion se procede a verificar la fecha y si ya paso las 24H minimas se modifica la info
            elif exist and len(self.__timeLocations.keys()) >= 1:

                timeNow = dt.datetime.now()
                restDay = timeNow - self.__timeLocations["dateCompled"]

                if(restDay.days > 1):
                    self.__timeLocations = {
                        "dateCompled" : timeNow,
                        "date": timeNow.strftime("%x"),
                        "hour": timeNow.strftime("%X")
                    }
                    self.__location = location
                    print(f"Se modifico su ubicacion de sucursal, ahora es: {location}")
                    self.setMoviemientos(dates)
                    return
                else:
                    print("No han pasado 24 horas minimas")
                    return
            
            print(f"Lo sentimos, la sucursal {location} no esta en la lista")

        except AttributeError: #caturamos el error por digitos numericos
            print("ERROR: No se permite numeros en la sucursal")

    

