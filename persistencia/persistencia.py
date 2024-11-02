import bd.bd as BD
from typing import List, Union


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

