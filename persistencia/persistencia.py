import bd.bd as BD
from typing import List, Union
import bcrypt , time


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


def viewUser(query,data,password):

    connet = BD.CNX()
    cursor = connet.cursor()

    cursor.execute(query,data)
    result = cursor.fetchone()

    if result == None:
        print("I'm really sorry, this list is null")
        return
    
    contra = f"{result[-1]}".encode("utf-8")

    if bcrypt.checkpw(password, contra):
        print("This password is validated...")
        time.sleep(2)
        print(result)
    else:
        print("This password is not validated")

    cursor.close()
    connet.close()
