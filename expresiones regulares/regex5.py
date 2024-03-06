import re

text = "Este es un ejemplo de una página web: https://id.fiscaliamichoacan.gob.mx/inicio y también podemos visitar la"
# ? valida que lo de anterior puede traer 1 o ninguna coincidencia

pattern = r"https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

result = re.findall(pattern, text)

print(result)