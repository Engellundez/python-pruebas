import re
email = "example_hola@example.com"

pattern =r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
# - sirve para hacer separaciones
# % "comodín" valida lo que tiene antes y después 
# + 1 o más coincidencias
result = re.match(pattern, email)

if result:
    print("valido")
else:
    print("invalido")