import bd.bd as BD
from typing import List, Union
import bcrypt 

async def data() -> List[object]:
    connet = BD.CNX()
    cursor = connet.cursor()

    query = "SELECT * FROM `usuarios`;"

    cursor.execute(query)
    data = cursor.fetchall()

    return data



def createUser(query:str, data:List[Union[str,int,float]]):

    try: 
        connet = BD.CNX()
        cursor = connet.cursor()
        cursor.execute(query,data)
        connet.commit()
        cursor.close()
        connet.close()
        print("User created successfully")
    except Exception as e:
        print("I'm really sorry, we are not create your account")
        print(e)


def viewUser(query:str, data:List[str], password:str) -> bool:

    connet = BD.CNX()
    cursor = connet.cursor()

    cursor.execute(query,data)
    result = cursor.fetchone()

    if result == None:
        print("I'm really sorry, this list is null")
        return False
    
    contra = f"{result[-1]}".encode("utf-8")

    if bcrypt.checkpw(password, contra):
        print("This password is validated...")
        cursor.close()
        connet.close()
        return True
    
    print("This password is not validated")
    cursor.close()
    connet.close()
    return False