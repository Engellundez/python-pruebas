import re

text = "Hola Pedro, mi numero es: +52 443 386 7825"
# ? valida que lo de anterior puede traer 1 o ninguna coincidencia

pattern = r"\+\d{1,}\s\d{3}\s\d{3}\s\d{4}"

remplazo = re.sub(pattern, "(Número oculto)", text)

print(remplazo)