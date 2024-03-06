import re

text = "La fecha es 05/03/2024 y el teléfono es +52-443-386-7825"

pattern = r"\d{2}/\d{2}/\d{4}"

replacement = "Fecha Oculta 👀"

new_text = re.sub(pattern, replacement, text)

print("Texto modificado: ", new_text)

