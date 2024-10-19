# import bd.bd as BD

# cursor = BD.CNX.cursor()
# sentecia = ("INSERT INTO `usuarios` (`id`, `name`, `age`, `cash`, `address`, `phone`, `email`, `location`, `ahorros`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);")
# DATA = [idUser, name, age, cash, adress, phone, email, savings]
# try:
#     cursor.execute(sentecia,DATA)
#     BD.CNX.commit()
#     cursor.close()
#     BD.CNX.close()
#     print("User created successfully")
# except ValueError:
#     print("I'm really sorry, we are not create your account")