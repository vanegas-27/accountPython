# En este ejercicio debemos de construir un software que permita gestionar las funciones cotidianas de una cuenta bancaria. tales como...

> envio y retiro de dinero

> consultar datos

> poder mover el dinero a "dinero de ahorros" y viceversa

> ver movimientos de cuenta

> Cambiar datos usuario

- este se debe de modelar en MVC para hacerlo mucho mas entendible
- se debe de implementar una clase
- manejar los errores debidamente
- se debe de crear la cuenta como clase para asi brindar mas seguridad y escalibilidad

## requisitos para crear cuenta

- identificacion
- nombre completo
- minimo inicial de 50COP
- ser mayor de edad
- ubicacion(direccion)
- telefono
- correo

> al crearse el usuario se le asigna un corresponsal por default(aleatorio) sucusales disponibles:      

- Medellin
- Sabaneta
- Envigado
- Itagui
- Bello
- Copacabana

> el usuario puede cambiar la sucursal donde lo atienden(si lo cambia no lo podria volver a hacer durante 24 horas)