import bd.bd as BD
from typing import List, Union


def createUser(query:str, data:List[Union[str,int,float]]):

    try: 
        conexion = BD.CNX()
        cursor = conexion.cursor()
        cursor.execute(query,data)
        conexion.commit()
        cursor.close()
        conexion.close()
        print("User created successfully")
    except Exception as e:
        print("I'm really sorry, we are not create your account")
        print(e)

